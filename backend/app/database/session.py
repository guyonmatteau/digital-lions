from functools import lru_cache
from typing import Annotated

from alembic import command
from alembic.config import Config
from core.settings import get_settings
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine


@lru_cache
def get_engine():
    """Get a cached database engine."""
    settings = get_settings()
    return create_engine(settings.POSTGRES_DATABASE_URL)


def init_db():
    """Setup db and create tables"""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def run_migrations():
    """Run migrations with Alembic"""
    alembic_cfg = Config("alemibic.ini")
    command.upgrade(alembic_cfg, "head")


def get_session() -> Session:
    """Get a database session.

    Args:
        engine: SQLModel engine."""
    engine = get_engine()
    session = Session(bind=engine, autocommit=False, autoflush=False)
    try:
        yield session
    finally:
        # close connection at end of request
        session.close()


SessionDependency = Annotated[Session, Depends(get_session)]
