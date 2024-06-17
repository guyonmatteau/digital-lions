from __future__ import annotations

from models.base import CreatedAt, UpdatedAt
from sqlmodel import Field, SQLModel


class CommunityBase(SQLModel, CreatedAt, UpdatedAt):
    name: str


class Community(CommunityBase, table=True):
    """Schema for community in database."""

    # __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)

    # workshops: list[Workshop] | None = Relationship(back_populates="community")


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(SQLModel, UpdatedAt):
    """Schema for updating a community."""

    name: str | None = None
    is_active: bool | None = None
