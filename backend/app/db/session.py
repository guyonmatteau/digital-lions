import logging
import os
from functools import lru_cache

from alembic import command
from alembic.config import Config
from sqlmodel import Session, SQLModel, create_engine

from app.settings import get_settings


@lru_cache()
def get_engine():
    settings = get_settings()
    return create_engine(settings.postgres_url)


def init_db():
    """Setup db and create tables"""
    settings = get_settings()
    engine = get_engine()

    SQLModel.metadata.create_all(engine)


def run_migrations():
    """Run migrations with Alembic"""
    alembic_cfg = Config("alemibic.ini")
    import pdb; pdb.set_trace()
    command.upgrade(alembic_cfg, "head")


def get_db():
    engine = get_engine()
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
