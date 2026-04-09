"""OAuth 2.1 token verification for GhostLabs MCP servers.

Validates JWT tokens from any OAuth 2.1 / OIDC provider (Auth0, Okta, self-hosted).
Tokens are validated against the provider's JWKS endpoint.
Falls back to static API key validation for backward compatibility.
"""
import os
import time
import logging
from typing import Any

import httpx
import jwt as pyjwt

logger = logging.getLogger(__name__)

# Cache JWKS keys for 1 hour
_jwks_cache: dict[str, Any] = {}
_jwks_cache_expiry: float = 0
JWKS_CACHE_TTL = 3600


async def _fetch_jwks(jwks_url: str) -> dict:
    """Fetch and cache JWKS from the OAuth provider."""
    global _jwks_cache, _jwks_cache_expiry

    if _jwks_cache and time.time() < _jwks_cache_expiry:
        return _jwks_cache

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(jwks_url)
        resp.raise_for_status()
        _jwks_cache = resp.json()
        _jwks_cache_expiry = time.time() + JWKS_CACHE_TTL
        return _jwks_cache


class GhostLabsTokenVerifier:
    """Verifies OAuth 2.1 JWT tokens for MCP server access.

    Supports two modes:
    1. JWT validation via JWKS endpoint (production -- set OAUTH_JWKS_URL)
    2. Static API key fallback (development -- set MCP_API_KEYS)

    Environment variables:
        OAUTH_ISSUER_URL: OAuth provider issuer URL (e.g., https://ghostlabs.auth0.com/)
        OAUTH_JWKS_URL: JWKS endpoint (e.g., https://ghostlabs.auth0.com/.well-known/jwks.json)
        OAUTH_AUDIENCE: Expected audience claim (e.g., https://mcp.ghostlabs.ai)
        MCP_API_KEYS: Comma-separated static API keys for development fallback
    """

    def __init__(self, required_scopes: list[str] | None = None):
        self.issuer = os.environ.get("OAUTH_ISSUER_URL", "")
        self.jwks_url = os.environ.get("OAUTH_JWKS_URL", "")
        self.audience = os.environ.get("OAUTH_AUDIENCE", "https://mcp.ghostlabs.ai")
        self.static_keys = [
            k.strip() for k in os.environ.get("MCP_API_KEYS", "").split(",") if k.strip()
        ]
        self.required_scopes = required_scopes or []

        # Determine mode
        self.jwt_mode = bool(self.jwks_url)
        if not self.jwt_mode and not self.static_keys:
            logger.warning(
                "No OAuth JWKS URL or static API keys configured. "
                "Set OAUTH_JWKS_URL for production or MCP_API_KEYS for development."
            )

    async def verify_token(self, token: str) -> dict | None:
        """Verify a Bearer token. Returns token claims if valid, None if invalid.

        In JWT mode: validates signature, expiry, issuer, audience, and scopes.
        In static mode: checks against MCP_API_KEYS list.
        """
        if not token:
            return None

        # Try JWT validation first
        if self.jwt_mode:
            return await self._verify_jwt(token)

        # Fallback to static API key
        if token in self.static_keys:
            return {"sub": "api-key", "scope": "admin", "client_id": "static"}

        return None

    async def _verify_jwt(self, token: str) -> dict | None:
        """Validate a JWT token against the JWKS endpoint."""
        try:
            jwks = await _fetch_jwks(self.jwks_url)

            # Decode header to find the signing key
            unverified_header = pyjwt.get_unverified_header(token)
            kid = unverified_header.get("kid")

            # Find matching key in JWKS
            signing_key = None
            for key in jwks.get("keys", []):
                if key.get("kid") == kid:
                    signing_key = pyjwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break

            if not signing_key:
                logger.warning("No matching key found in JWKS for kid=%s", kid)
                return None

            # Verify and decode
            claims = pyjwt.decode(
                token,
                signing_key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=self.issuer,
                options={"verify_exp": True, "verify_aud": True, "verify_iss": bool(self.issuer)},
            )

            # Check scopes
            if self.required_scopes:
                token_scopes = claims.get("scope", "").split()
                if not all(s in token_scopes for s in self.required_scopes):
                    logger.warning(
                        "Token missing required scopes. Has: %s, needs: %s",
                        token_scopes, self.required_scopes,
                    )
                    return None

            return claims

        except pyjwt.ExpiredSignatureError:
            logger.debug("Token expired")
            return None
        except pyjwt.InvalidTokenError as e:
            logger.debug("Invalid token: %s", e)
            return None
        except Exception as e:
            logger.warning("Token verification error: %s", e, exc_info=True)
            return None
