from pydantic import field_validator
from sqlmodel import Field, SQLModel, Relationship


class AttendanceBase(SQLModel):
    """Base class for attendance model."""

    child_id: int = Field(foreign_key="child.id")
    attendance: str

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError(
                "Attendance must be either 'present' or 'absent' or 'cancelled'"
            )
        return v


class AttendanceCreate(AttendanceBase):
    """Data model for creating an attendance."""

    workshop_id: int = Field(foreign_key="workshop.id")



class Attendance(AttendanceCreate, table=True):
    """Data model for attenadance of a child in a workshop."""

    id: int = Field(default=None, primary_key=True)


