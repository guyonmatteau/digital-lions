import logging
from typing import Annotated, Any

from core.settings import Settings, get_settings
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import APIKeyHeader

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

    _API_KEY = "API-Key"

    def __init__(
        self,
        auto_error: bool = True,
    ):
        super().__init__(auto_error=auto_error, name=self._API_KEY)

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


APIKeyDependency = Depends(APIKeyHandler())
