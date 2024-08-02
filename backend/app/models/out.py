"""Models for responses to the client. All in one module to avoid circular imports."""

from __future__ import annotations

from models.api.generic import MetadataColumns
from models.workshop import WorkshopBase
from pydantic import BaseModel, EmailStr, Field, field_validator
from sqlmodel import AutoString


class UserBase(BaseModel):
    first_name: str
    last_name: str = Field(default=None)
    email_address: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    role: str | None = Field(default=None, description="User role on platform")


class CommunityBase(BaseModel):
    name: str


class AttendanceBase(BaseModel):
    """Base class for attendance model."""

    attendance: str

    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
        return v


class RecordCreated(BaseModel):
    id: int


class ChildBase(BaseModel):
    """Base schema for child model."""

    first_name: str
    last_name: str


class ChildPersonalInfo:
    """Additional information about child."""

    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(default=None, description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child. Either male or female.")


# each model has two output types to be returned by the API:
# base, to be used as object in a list, only containing basic info
# full to be used as objectOut on GET by ID


class ChildOut(ChildBase, ChildPersonalInfo, MetadataColumns):
    """Response model containing all info on a child,
    including relations like team community, and metadata."""

    id: int


class ChildOutBasic(ChildBase):
    """Response model containing only basic properties, to be used when
    returning a list of objects."""

    id: int


class AttendanceOutWithChild(AttendanceBase):
    child: ChildOut
    workshop: WorkshopOutForAttendance


class CommunityOutBasic(CommunityBase):
    id: int


class CommunityOutGetById(CommunityOutBasic, MetadataColumns):
    """Response model for GET /communities/:id"""

    pass


class UserOut(UserBase):
    id: int


class WorkshopOut(WorkshopBase):
    id: int
    team_id: int


class ChildOutSimple(BaseModel):
    id: int
    first_name: str
    last_name: str


class AttendanceForWorkshop(BaseModel):
    attendance: str
    child: ChildOutSimple


class WorkshopOutWithAttendance(WorkshopOut, WorkshopBase):
    attendance: list[AttendanceForWorkshop]


class WorkshopOutForAttendance(WorkshopOut):
    id: int
