from datetime import datetime
from typing import List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class CommunityCreate(SQLModel):
    name: str = Field()


class Community(CommunityCreate, table=True):
    """Community model."""
    id: int = Field(default=None, primary_key=True)
    is_active: bool = True

    workshops: list["Workshop"] | None = Relationship(back_populates="community")

    created_at: datetime = datetime.now()
    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()
