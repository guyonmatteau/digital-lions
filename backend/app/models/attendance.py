from pydantic import field_validator
from sqlmodel import Field, SQLModel, Relationship
from models.base import AttendanceBase
from models.child import Child
from models.workshop import Workshop


class AttendanceCreate(AttendanceBase):
    """Data model for creating an attendance."""

    workshop_id: int = Field(foreign_key="workshop.id")


class Attendance(AttendanceCreate, table=True):
    """Data model for attenadance of a child in a workshop."""

    id: int = Field(default=None, primary_key=True)
    child: Child = Relationship(back_populates="attendances")
    workshop: Workshop = Relationship(back_populates="attendances")
