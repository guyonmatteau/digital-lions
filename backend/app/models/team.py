from __future__ import annotations

from pydantic import ConfigDict
from sqlalchemy.orm import Mapped
from typing import List

# from models.base import CreatedAt, UpdatedAt
from sqlmodel import Field, Relationship, SQLModel


class TeamBase(SQLModel):
    # , CreatedAt, UpdatedAt):
    """Base class for team model."""

    name: str = Field(description="Name of the team", default=None, nullable=True)
    community_id: int = Field(
        description="ID of community the team is in", foreign_key="communities.id"
    )


class TeamCreateChild:
    """Data model to create a child within a team."""

    first_name: str
    last_name: str
    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(default=None, description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child")


class TeamCreate(TeamBase):
    """Data model for creating a team."""

    # model_config = ConfigDict(arbitrary_types_allowed=True)
    # ig:
    #     arbitrary_types_allowed=True
    # children: list[TeamCreateChild] | None = Field(
    #     description="List of children to create within the team", default=None
    # )
    #


class Team(TeamCreate, table=True):
    """Data model for teams. A team is a group of children that
    follow the Little Lions program: a set of workshops. The workshops
    that the team follows are linked to the team as well."""

    # __table_args__ = {"extend_existing": True}
    __tablename__ = "teams"

    id: int = Field(default=None, primary_key=True)
    program_tracker: int = Field(
        description="The current workshop the team is at in the program", default=1
    )
    community_id: int = Field(foreign_key="communities.id")
    community: Mapped["Community"] = Relationship(back_populates="teams")
    # children: list[Child] | None = Relationship(
    #     back_populates="team"
    # )  # children: list[Child] | None = Relationship(back_populates="team")
    # community: Community = Relationship(back_populates="teams")
    # program: Program = Relationship(back_populates="teams")
    # workshops: list[Workshop] | None = Relationship(back_populates="team")


class TeamUpdate:
    # , CreatedAt, UpdatedAt):
    """Data model for updating a team."""

    name: str = Field(description="Name of the team", nullable=True)
    community_id: int = Field(
        description="ID of community the team is in", foreign_key="communites.id"
    )
