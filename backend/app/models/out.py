"""Models for responses to the client. All in one module to avoid circular imports."""

from __future__ import annotations

from models.attendance import AttendanceBase
from models.base import MetadataColumns
from models.community import CommunityBase
from models.team import TeamBase
from models.user import UserBase
from models.workshop import WorkshopBase
from pydantic import BaseModel, Field


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


class TeamOut(TeamBase, MetadataColumns):
    """Response model containing all info on a team, including
    children in it, workshops, etc."""

    id: int
    children: list[ChildOutBasic]
    community: CommunityOutBasic


class TeamOutBasic(TeamBase):
    """Response model containing basic properties of a team."""

    id: int


class AttendanceOutWithChild(AttendanceBase):
    child: ChildOut
    workshop: WorkshopOutForAttendance


class CommunityOutBasic(CommunityBase):
    id: int


class CommunityOutGetById(CommunityOutBasic, MetadataColumns):
    """Response model or GET /communities/:id"""

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
