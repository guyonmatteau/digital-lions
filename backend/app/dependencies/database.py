from functools import lru_cache
from typing import Annotated

from alembic import command
from alembic.config import Config
from fastapi import Depends
from settings import get_settings
from sqlmodel import Session, SQLModel, create_engine


@lru_cache
def get_engine():
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


def get_database():
    engine = get_engine()
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


DatabaseDependency = Annotated[Session, Depends(get_database)]
