import logging
import os

from alembic import command
from alembic.config import Config

from sqlmodel import Session, SQLModel, create_engine

from app.settings import get_settings


def create_db_and_tables():
    """Setup db and create tables"""
    settings = get_settings()
    engine = create_engine(settings.postgres_url)

    SQLModel.metadata.create_all(engine)


def run_migrations():
    """Run migrations with Alembic"""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
