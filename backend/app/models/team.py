from typing import TYPE_CHECKING

from models.base import CreateProperties, MetadataColumns, UpdateProperties
from pydantic import BaseModel
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.child import Child
    from models.community import Community
    from models.workshop import Workshop


class TeamBase(SQLModel):
    """Base class for team model."""

    name: str = Field(description="Name of the team")


class TeamCreateChild(BaseModel, CreateProperties):
    """Data model to create a child within a team."""

    first_name: str
    last_name: str
    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(default=None, description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child")
    team_id: int | None = Field(description="ID of the team the child belongs to", default=None)


class TeamCreate(TeamBase, CreateProperties):
    """Data model for creating a team."""

    class Config:
        arbitrary_types_allowed = True

    children: list[TeamCreateChild] | None
    community_id: int = Field(foreign_key="communities.id")


class Team(TeamBase, MetadataColumns, table=True):
    """Data model for teams. A team is a group of children that
    follow the Little Lions program: a set of workshops. The workshops
    that the team follows are linked to the team as well."""

    __tablename__ = "teams"

    id: int = Field(default=None, primary_key=True)
    program_tracker: int = Field(
        description="The current workshop the team is at in the program", default=1
    )

    community_id: int = Field(foreign_key="communities.id")
    community: "Community" = Relationship(back_populates="teams")
    children: list["Child"] | None = Relationship(back_populates="team")
    workshops: list["Workshop"] | None = Relationship(back_populates="team")


class TeamUpdate(UpdateProperties):
    """Data model for updating a team."""

    name: str | None = None
    community_id: int | None = None
