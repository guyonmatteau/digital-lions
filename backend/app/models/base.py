# to avoid circular imports put all base models and out models
# in this separate models. TO DO fix.
from typing import Optional, List

from pydantic import field_validator
from sqlmodel import Field, SQLModel, Relationship


class CommunityBase(SQLModel):
    name: str


class ChildBase(SQLModel):
    """Base schema for child model."""

    first_name: str
    last_name: str
    age: Optional[int] = Field(
        default=None, description="Age in years at the time of registration"
    )


class AttendanceBase(SQLModel):
    """Base class for attendance model."""

    child_id: int = Field(foreign_key="child.id", exclude=True)
    attendance: str

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError(
                "Attendance must be either 'present' or 'absent' or 'cancelled'"
            )
        return v


class WorkshopBaseBase(SQLModel):
    date: str = Field(description="The date of the workshop in the format YYYY-MM-DD")
    cycle: Optional[int] = Field(
        default=None, description="The cycle of the workshop", nullable=True
    )


class WorkshopBase(WorkshopBaseBase):
    cancelled: bool = Field(
        default=False, description="Whether the workshop was cancelled or not"
    )
    cancellation_reason: Optional[str] = Field(
        default=None,
        description="The reason for the cancellation, if any",
        nullable=True,
    )


class CommunityOut(CommunityBase):
    # workshops and children should not be part of out
    id: int


class WorkshopOut(WorkshopBaseBase):
    id: int
    community: CommunityOut


class WorkshopOutWithAttendance(WorkshopOut, WorkshopBaseBase):
    attendance: List[AttendanceBase]


class WorkshopOutForAttendance(WorkshopOut):
    id: int


class ChildOut(ChildBase):
    id: int


class ChildOutWithCommunity(ChildOut):
    community: CommunityOut


class AttendanceOutWithChild(AttendanceBase):
    child: ChildOut
    workshop: WorkshopOutForAttendance = []
