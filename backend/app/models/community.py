from datetime import datetime

from models.base import CommunityBase
from sqlmodel import Field, Relationship, SQLModel


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(CommunityCreate):
    """Schema for updating a community."""

    is_active: bool = True


class Community(CommunityUpdate, table=True):
    """Schema for community in database."""

    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)

    workshops: list["Workshop"] | None = Relationship(back_populates="community")
    children: list["Child"] | None = Relationship(back_populates="community")

    created_at: datetime = datetime.now()
    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()
