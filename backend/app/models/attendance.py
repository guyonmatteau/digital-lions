from datetime import datetime
from typing import List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class Attendance(SQLModel, table=True):
    """Data model for attenadance of a child in a workshop."""

    id: int = Field(primary_key=True)
    child_id: int = Field(foreign_key="child.id")
    workshop_id: int = Field(foreign_key="workshop.id")
    attendance: str

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError(
                "Attendance must be either 'present' or 'absent' or 'cancelled'"
            )
        return v

    # workshop: Workshop = Relationship(back_populates="attendance")
