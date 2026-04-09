"""OAuth 2.1 middleware for FastMCP servers."""
import logging
from .token_verifier import GhostLabsTokenVerifier

logger = logging.getLogger(__name__)


class OAuthMiddleware:
    """FastMCP middleware that validates OAuth tokens on every request.

    Extracts Bearer token from the Authorization header, validates via
    GhostLabsTokenVerifier, and rejects unauthorized requests.
    """

    def __init__(self, verifier: GhostLabsTokenVerifier):
        self.verifier = verifier

    async def __call__(self, request, call_next):
        """Validate token before passing to the tool handler."""
        # Extract token from Authorization header
        auth_header = ""
        if hasattr(request, "headers"):
            auth_header = request.headers.get("authorization", "")
        elif hasattr(request, "meta"):
            auth_header = request.meta.get("authorization", "")

        token = auth_header.replace("Bearer ", "").strip() if auth_header.startswith("Bearer ") else ""

        # Skip auth if no OAuth is configured (development mode)
        if not self.verifier.jwt_mode and not self.verifier.static_keys:
            return await call_next(request)

        # Validate token
        claims = await self.verifier.verify_token(token)
        if claims is None:
            raise Exception("Unauthorized: Invalid or missing OAuth 2.1 token")

        return await call_next(request)
