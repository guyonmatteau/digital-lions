from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from models.attendance import AttendanceBase


class WorkshopBase(SQLModel):
    date: str = Field(description="The date of the workshop in the format YYYY-MM-DD")
    cycle: Optional[int] = Field(
        default=None, description="The cycle of the workshop", nullable=True
    )
    cancelled: bool = Field(
        default=False, description="Whether the workshop was cancelled or not"
    )
    cancellation_reason: Optional[str] = Field(
        default=None,
        description="The reason for the cancellation, if any",
        nullable=True,
    )


class WorkshopCreate(WorkshopBase):
    community_id: int
    attendance: Optional[list[AttendanceBase]] = None


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    id: int = Field(default=None, primary_key=True)

    community_id: int = Field(foreign_key="community.id")
    # community: Community | None = Relationship(back_populates="workshops")
