from __future__ import annotations
from typing import List

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from sqlalchemy.orm import Mapped


class CommunityBase(SQLModel):
    name: str
    is_active: bool = True
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()


class Community(SQLModel, table=True):
    """Schema for community in database."""

    # __table_args__ = {"extend_existing": True}
    __tablename__ = "communities"
    id: int = Field(default=None, primary_key=True)

    teams: Mapped[List["Team"]] = Relationship(back_populates="community")

    # workshops: list[Workshop] | None = Relationship(back_populates="community")


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(SQLModel):
    """Schema for updating a community."""

    name: str | None = None
    is_active: bool | None = None
