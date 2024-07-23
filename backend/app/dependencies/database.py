from functools import lru_cache
from typing import Annotated

from alembic import command
from alembic.config import Config
from fastapi import Depends
from settings import get_settings
from sqlmodel import Session, SQLModel, create_engine


@lru_cache
def get_engine():
    """Get a cached database engine."""
    settings = get_settings()
    return create_engine(settings.postgres_url)


def init_db():
    """Setup db and create tables"""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def run_migrations():
    """Run migrations with Alembic"""
    alembic_cfg = Config("alemibic.ini")
    command.upgrade(alembic_cfg, "head")


def get_database() -> Session:
    """Get a database session"""
    engine = get_engine()
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


def get_session() -> Session:
    """Get a database session.

    Args:
        engine: SQLModel engine."""
    engine = get_engine()
    session = Session(bind=engine, autocommit=False, autoflush=False)
    yield session


SessionDependency = Annotated[Session, Depends(get_session)]
DatabaseDependency = Annotated[Session, Depends(get_database)]
