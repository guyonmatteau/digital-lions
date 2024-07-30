import datetime
from typing import TYPE_CHECKING

from models.base import MetadataColumns
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class Child(SQLModel, MetadataColumns, table=True):
    """Schema for child model in database."""

    __tablename__ = "children"
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str

    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(default=None, description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child. Either male or female.")

    team: "Team" = Relationship(back_populates="children")
    team_id: int = Field(foreign_key="teams.id")
    attendances: list["Attendance"] = Relationship(back_populates="child")
