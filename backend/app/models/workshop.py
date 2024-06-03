from typing import List, Optional

from app.models.base import AttendanceBase, WorkshopBase
from app.models.community import Community
from sqlmodel import Field, Relationship, SQLModel


class WorkshopCreate(WorkshopBase):
    community_id: int
    attendance: Optional[List[AttendanceBase]]


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    id: int = Field(default=None, primary_key=True)

    community_id: int = Field(foreign_key="community.id")
    community: Community | None = Relationship(back_populates="workshops")

    attendances: List["Attendance"] = Relationship(back_populates="workshop")
