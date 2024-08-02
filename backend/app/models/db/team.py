from typing import TYPE_CHECKING

from models.base import MetadataColumns
from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.child import Child
    from models.community import Community
    from models.workshop import Workshop


class Team(SQLModel, MetadataColumns, table=True):
    """Data model for teams. A team is a group of children that
    follow the Little Lions program: a set of workshops. The workshops
    that the team follows are linked to the team as well."""

    __tablename__ = "teams"

    id: int = Field(default=None, primary_key=True)
    name: str = Field(description="Name of the team")

    community_id: int = Field(
        sa_column=Column(Integer, ForeignKey("communities.id", ondelete="CASCADE"))
    )
    community: "Community" = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="teams"
    )
    children: list["Child"] | None = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="team"
    )
    workshops: list["Workshop"] | None = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="team"
    )
