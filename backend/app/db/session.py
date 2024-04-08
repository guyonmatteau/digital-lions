import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL


def postgres_url() -> str:
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
    database = "digitallions"
    url = URL.create(
        drivername=scheme,
        username=username,
        password=password,
        host=host,
        port=5432,
        database=database,
    )
    return url


engine = create_engine(postgres_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
