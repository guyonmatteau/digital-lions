from app.models.base import AttendanceBase
from app.models.child import Child
from app.models.workshop import Workshop
from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class AttendanceCreate(AttendanceBase):
    """Data model for creating an attendance."""

    workshop_id: int = Field(foreign_key="workshop.id")


class Attendance(AttendanceCreate, table=True):
    """Data model for attenadance of a child in a workshop."""

    id: int = Field(default=None, primary_key=True)
    child: Child = Relationship(back_populates="attendances")
    workshop: Workshop = Relationship(back_populates="attendances")
