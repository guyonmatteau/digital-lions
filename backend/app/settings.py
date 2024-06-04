import logging
import os
from functools import lru_cache

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    scheme: str = "postgresql"
    database: str = "digitallions"

    @computed_field
    @property
    def postgres_url(self) -> str:
        database_url = os.environ.get("POSTGRES_DATABASE_URL")
        if database_url is not None:
            logging.info(f"Using database URL from environment: {database_url}")
            return database_url

        logging.info("Building database URL from environment variables")
        username = os.environ.get("POSTGRES_USER")
        if username is None:
            raise ValueError("POSTGRES_USER is not set")
        password = os.environ.get("POSTGRES_PASSWORD")
        if password is None:
            raise ValueError("POSTGRES_PASSWORD is not set")
        host = os.environ.get("POSTGRES_HOST")
        if host is None:
            raise ValueError("POSTGRES_HOST is not set")
        port = os.environ.get("POSTGRES_PORT")
        if port is None:
            raise ValueError("POSTGRES_PORT is not set")

        url = f"{self.scheme}://{username}:{password}@{host}:{port}/{self.database}"
        return url


@lru_cache
def get_settings():
    return Settings()
