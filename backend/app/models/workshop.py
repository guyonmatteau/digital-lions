from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from models.base import WorkshopBase, AttendanceBase
from models.community import Community


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
