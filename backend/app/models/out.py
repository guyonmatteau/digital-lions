"""Models for responses to the client. In separate files to avoid circular imports."""

from __future__ import annotations

# from models.attendance import AttendanceBase
from models.child import ChildBase
from models.community import CommunityBase

# from models.workshop import WorkshopBase


# class AttendanceOutWithChild(AttendanceBase):
#     child: ChildOut
#     workshop: WorkshopOutForAttendance
#


class ChildOut(ChildBase):
    id: int


class ChildOutWithCommunity(ChildOut):
    community: CommunityOut


class CommunityOut(CommunityBase):
    id: int


# class UserOut(UserBase):
#     id: int
#
#
# class WorkshopOut(WorkshopBase):
#     id: int
#     community: CommunityOut
#
#
# class WorkshopOutWithAttendance(WorkshopOut, WorkshopBase):
#     attendance: List[AttendanceBase]
#
#
# class WorkshopOutForAttendance(WorkshopOut):
#     id: int
