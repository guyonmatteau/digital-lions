from typing import TYPE_CHECKING

from models.base import CreateProperties, MetadataColumns, UpdateProperties
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.team import Team


class CommunityBase(SQLModel):
    name: str


class Community(CommunityBase, MetadataColumns, table=True):
    """Schema for community in database."""

    __tablename__ = "communities"
    id: int = Field(default=None, primary_key=True)

    teams: list["Team"] = Relationship(back_populates="community")


class CommunityCreate(CommunityBase, CreateProperties):
    pass


class CommunityUpdate(SQLModel, UpdateProperties):
    """Schema for updating a community."""

    name: str | None = None
