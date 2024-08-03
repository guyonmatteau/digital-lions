import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class Workshop(SQLModel, table=True):
    """Data model for workshops. A workshop is a session that took place with a team
    on a given date in a given community."""

    __tablename__ = "workshops"
    __table__args__ = (
        UniqueConstraint(
            "team_id", "workshop_number", name="unique_workshop_number_per_team"
        ),
    )

    date: datetime.date = Field(
        description="The date of the workshop in the format YYYY-MM-DD"
    )
    workshop_number: int = Field(
        description="The number of the workshop in the program"
    )

    id: int = Field(default=None, primary_key=True)
    team_id: int = Field(
        sa_column=Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"))
    )

    team: "Team" = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="workshops"
    )
    attendance: list["Attendance"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="workshop"
    )
