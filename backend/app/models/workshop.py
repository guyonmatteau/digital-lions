# from models.attendance import AttendanceBase
# from models.community import Community, CommunityOut
from typing import TYPE_CHECKING

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class WorkshopBase(SQLModel):
    date: str = Field(
        description="The date of the workshop in the format YYYY-MM-DD")
    cancelled: bool = Field(
        default=False, description="Whether the workshop was cancelled or not")
    cancellation_reason: str | None = Field(
        default=None,
        description="The reason for the cancellation, if any",
        nullable=True,
    )


class WorkshopCreateAttendance(SQLModel):
    """Model for adding attendance to a workshop."""

    attendance: str
    child_id: int = Field(foreign_key="children.id")
    workshop_id: int = Field(foreign_key="workshops.id", default=None)

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError(
                "Attendance must be either 'present' or 'absent' or 'cancelled'")
        return v


class WorkshopCreate(WorkshopBase):
    class Config:
        arbitrary_types_allowed = True

    team_id: int | None = Field(foreign_key="teams.id", default=None)
    attendance: list[WorkshopCreateAttendance] | None


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place with a team
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    __tablename__ = "workshops"

    id: int = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="teams.id")
    team: "Team" = Relationship(back_populates="workshops")
    attendance: list["Attendance"] = Relationship(back_populates="workshop")
