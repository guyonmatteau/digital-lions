import logging
from typing import Annotated, Any

from core.settings import Settings, get_settings
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer

logger = logging.getLogger(__name__)


class APIKeyHandler(APIKeyHeader):
    """FastAPI dependency for API key header.

    Requirement of this header is enabled/disabled in the backend
    via environment variable `FEATURE_API_KEY`.
    Headers to be sent in the request:
    ```
    headers = {
        "API-Key": {API_KEY},
    }
    ```
    """

    API_KEY = "API-Key"

    def __init__(
        self,
        auto_error: bool = True,
    ):
        super().__init__(auto_error=auto_error, name=self.API_KEY)

    async def __call__(
        self, request: Request, settings: Annotated[Settings, Depends(get_settings)]
    ) -> Any:
        self.settings = settings
        # conditional check for API key requirement
        if not self.settings.FEATURE_API_KEY:
            return

        api_key: str = await super().__call__(request)
        self._verify_api_key(api_key)

    def _verify_api_key(self, key: str) -> True:
        """Verify the API key."""
        if key != self.settings.API_KEY:
            logger.error("Invalid API key")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API key")
        return True


class BearerTokenHandler(HTTPBearer):
    """FastAPI dependency for JWT token. Requirement of this token
    is enabled/disabled in the backend via environment variable `FEATURE_OAUTH`.
    A JWT is obtained from the /users/session endpoint.

    Headers to be sent in the request:
    ```
    headers = {
        "Authorization": Bearer {JWT},
    }
    ```
    """

    CREDENTIAL_SCHEME = "Bearer"

    def __init__(
        self,
        auto_error: bool = True,
    ):
        super().__init__(auto_error=auto_error)

    async def __call__(
        self, request: Request, settings: Annotated[Settings, Depends(get_settings)]
    ) -> Any:
        """Verify the bearer token and return the decoded token."""
        if not settings.FEATURE_OAUTH:
            return

        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == self.CREDENTIAL_SCHEME:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid authentication scheme.",
                )

            token_headers = self._get_unverified_headers(credentials.credentials)
            if token_headers is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Bearer token is no valid JWT.",
                )

            self.jwt_token_decoded = self._verify_jwt(token=credentials.credentials)
            if not self.jwt_token_decoded:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token.",
                )
            return self.jwt_token_decoded

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code."
        )

    def _verify_jwt(self, token: str) -> dict[str, Any] | None:
        """Verify the JWT token."""
        pass

    def _get_unverified_headers(self, token: str) -> dict[str, str] | None:
        """Get unverified token headers containing type,
        algorithm and key identifier."""
        pass


APIKeyDependency = Depends(APIKeyHandler())
BearerTokenDependency = Depends(BearerTokenHandler())
