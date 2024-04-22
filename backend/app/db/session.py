import os
import logging

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
if not database_exists(engine.url):
    logging.info("Creating database")
    create_database(engine.url)
else:
    logging.info("Database already exists")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
