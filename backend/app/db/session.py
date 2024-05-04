import logging
import os

from sqlmodel import Session, SQLModel, create_engine


def postgres_url() -> str:
    database_url = os.environ.get("POSTGRES_DATABASE_URL")
    if database_url is not None:
        logging.info(f"Using database URL from environment: {database_url}")
        return database_url

    logging.info("Building database URL from environment variables")
    scheme = "postgresql"
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
    database = "digitallions"

    url = f"postgresql://{username}:{password}@{host}:{port}/{database}"
    return url


engine = create_engine(postgres_url())


def create_db_and_tables():
    """Setup db and create tables"""
    SQLModel.metadata.create_all(engine)


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
