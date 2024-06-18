from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.team import Team


class CommunityBase(SQLModel):
    name: str
    is_active: bool = True
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()


class Community(CommunityBase, table=True):
    """Schema for community in database."""

    __tablename__ = "communities"
    id: int = Field(default=None, primary_key=True)

    teams: list["Team"] = Relationship(back_populates="community")
    # workshops: list[Workshop] | None = Relationship(back_populates="community")


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(SQLModel):
    """Schema for updating a community."""

    name: str | None = None
    is_active: bool | None = None
