"""OAuth 2.1 settings factory for MCP servers."""
import os


def get_auth_settings() -> dict:
    """Build auth configuration from environment variables.

    Returns dict suitable for FastMCP auth parameter, or empty dict if no OAuth configured.
    """
    issuer = os.environ.get("OAUTH_ISSUER_URL", "")
    if not issuer:
        return {}

    return {
        "issuer_url": issuer,
        "resource_server_url": os.environ.get("OAUTH_RESOURCE_URL", ""),
        "required_scopes": [
            s.strip() for s in os.environ.get("OAUTH_REQUIRED_SCOPES", "").split(",") if s.strip()
        ],
    }
