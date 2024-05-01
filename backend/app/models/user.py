from datetime import datetime
from typing import List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    email_address: str
    role: str | None = None
    is_active: bool = True
    created_at: datetime = datetime.now()

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()
