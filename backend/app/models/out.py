"""Models for responses to the client. All in one module to avoid circular imports."""

from __future__ import annotations

from models.attendance import AttendanceBase
from models.child import ChildBase
from models.community import CommunityBase
from models.team import TeamBase
from models.user import UserBase
from models.workshop import WorkshopBase
from pydantic import BaseModel


class RecordCreated(BaseModel):
    id: int


class AttendanceOutWithChild(AttendanceBase):
    child: ChildOut
    workshop: WorkshopOutForAttendance


class ChildOut(ChildBase):
    id: int


class ChildOutWithCommunity(ChildOut):
    community: CommunityOut


class ChildOutDeep(ChildOut):
    team: TeamOut


class CommunityOut(CommunityBase):
    id: int


class TeamOut(TeamBase):
    id: int
    children: list[ChildOut]
    community: CommunityOut


class UserOut(UserBase):
    id: int


class WorkshopOut(WorkshopBase):
    id: int
    community: CommunityOut


class WorkshopOutWithAttendance(WorkshopOut, WorkshopBase):
    attendance: List[AttendanceBase]


class WorkshopOutForAttendance(WorkshopOut):
    id: int
