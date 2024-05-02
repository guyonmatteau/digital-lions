from typing import Optional

from sqlmodel import Field, SQLModel

# from models.attendance import AttendanceCreate


class ChildAttendanceCreate(SQLModel):
    child_id: int
    attendance: str

class WorkshopBase(SQLModel):
    date: str = Field(description="The date of the workshop in the format YYYY-MM-DD")
    cycle: int
    cancelled: bool = Field(default=False, description="Whether the workshop was cancelled or not")
    cancellation_reason: str = Field(default=None, description="The reason for the cancellation, if any")


class WorkshopCreate(WorkshopBase):
    community_id: int

    attendance: Optional[list[ChildAttendanceCreate]] = None



class Workshop(SQLModel, table=True):
    """Data model for workshops. A workshop is a session that took place
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    id: int = Field(default=None, primary_key=True)
    date: str  # format YYYY-MM-DD
    cycle: int = None
    cancelled: bool
    cancellation_reason: str = None

    community_id: int = Field(foreign_key="community.id")
    # community: Community | None = Relationship(back_populates="workshops")
