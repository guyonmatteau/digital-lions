from __future__ import annotations

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from models.team import Team


class CommunityBase(SQLModel):
    name: str
    is_active: bool = True
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()


class Community(CommunityBase, table=True):
    """Schema for community in database."""

    # __table_args__ = {"extend_existing": True}
    __tablename__ = "communities"
    id: int = Field(default=None, primary_key=True)

    teams: list[Team] | None = Relationship(back_populates="community")

    # workshops: list[Workshop] | None = Relationship(back_populates="community")


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(SQLModel):
    """Schema for updating a community."""

    name: str | None = None
    is_active: bool | None = None
