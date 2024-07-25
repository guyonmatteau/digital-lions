import datetime
from typing import TYPE_CHECKING

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class WorkshopBase(SQLModel):
    date: datetime.date = Field(description="The date of the workshop in the format YYYY-MM-DD")
    workshop_number: int = Field(description="The number of the workshop in the program")

    @field_validator("workshop_number")
    def workshop_number_in_default_range(cls, v):
        """Validate that the workshop number is between 1 and 12."""
        if v not in range(1, 13):
            raise ValueError("Workshop number must be between 1 and 12.")
        return v


class WorkshopCreateAttendance(SQLModel):
    """Model for adding attendance to a workshop."""

    attendance: str
    child_id: int = Field(foreign_key="children.id")

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
        return v


class WorkshopCreateInDB(WorkshopBase):
    team_id: int = Field(foreign_key="teams.id")


class WorkshopCreateAttendanceInDB(WorkshopCreateAttendance):
    """Model for adding attendance to workshop in the context of a workshop."""

    workshop_id: int = Field(foreign_key="workshops.id", default=None)


class WorkshopCreate(WorkshopBase):
    class Config:
        arbitrary_types_allowed = True

    attendance: list[WorkshopCreateAttendance] | None


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place with a team
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    __tablename__ = "workshops"
    __table__args__ = (
        UniqueConstraint("team_id", "workshop_number", name="unique_workshop_number_per_team"),
    )

    id: int = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="teams.id")
    team: "Team" = Relationship(back_populates="workshops")
    attendance: list["Attendance"] = Relationship(back_populates="workshop")
