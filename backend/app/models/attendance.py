from typing import TYPE_CHECKING

from pydantic import Field, field_validator
from sqlmodel import Relationship, SQLModel

if TYPE_CHECKING:
    from models.child import Child
    from models.workshop import Workshop


# class AttendanceBase(SQLModel):
#     """Base class for attendance model."""
#
#     child_id: int = Field(foreign_key="children.id", exclude=True)
#     attendance: str
#
#     @field_validator("attendance")
#     def validate_attendance(cls, v):
#         if v not in ["present", "absent", "cancelled"]:
#             raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
#         return v
#
#
# class AttendanceCreate(AttendanceBase):
#     """Data model for creating an attendance."""
#
#     workshop_id: int = Field(foreign_key="workshops.id")
#

# class Attendance(SQLModel, table=True):
#     """Data model for attendance of a child in a workshop."""
#
#     __tablename__ = "attendances"
#
#     id: int = Field(default=None, primary_key=True)
#
#     child: "Child" = Relationship(back_populates="attendances")
#     workshop: "Workshop" = Relationship(back_populates="attendances")
