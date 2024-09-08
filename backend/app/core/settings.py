from functools import lru_cache
from typing import Any

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""

    model_config = SettingsConfigDict(case_sensitive=False)

    # database
    POSTGRES_DATABASE_URL: str

    # feature flags
    FEATURE_OAUTH: bool = False
    FEATURE_API_KEY: bool = True

    # security
    API_KEY: str = None

    # networking
    ALLOWED_ORIGINS: str
    ALLOWED_METHODS: str = "GET, POST, PATCH, PUT, DELETE, OPTIONS"
    ALLOWED_HEADERS: str = "Content-Type, Authorization"

    def model_post_init(self, __context) -> None:
        """Post init hook."""
        self.ALLOWED_METHODS = self.ALLOWED_METHODS.split(",")
        self.ALLOWED_HEADERS = self.ALLOWED_HEADERS.split(",")

    @model_validator(mode="after")
    def validate_api_key_settings(self) -> Any:
        """Validate the API key settings."""
        if self.FEATURE_API_KEY and not self.API_KEY:
            raise ValueError("FEATURE_API_KEY is True but API_KEY is not set")
        return self


@lru_cache
def get_settings():
    return Settings()
