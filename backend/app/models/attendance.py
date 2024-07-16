from typing import TYPE_CHECKING

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.child import Child
    from models.workshop import Workshop


class AttendanceBase(SQLModel):
    """Base class for attendance model."""

    attendance: str

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
        return v


class AttendanceCreate(AttendanceBase):
    """Data model for creating an attendance."""

    child_id: int = Field(foreign_key="children.id", exclude=True)
    workshop_id: int = Field(foreign_key="workshops.id")


class Attendance(AttendanceBase, table=True):
    """Data model for attendance of a child in a workshop."""

    __tablename__ = "attendances"

    id: int = Field(default=None, primary_key=True)

    child_id: int = Field(foreign_key="children.id")
    workshop_id: int = Field(foreign_key="workshops.id")

    child: "Child" = Relationship(back_populates="attendances")
    workshop: "Workshop" = Relationship(back_populates="attendance")
