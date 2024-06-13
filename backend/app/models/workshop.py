from __future__ import annotations

# from models.attendance import AttendanceBase
# from models.community import Community, CommunityOut
from sqlmodel import Field, Relationship, SQLModel


class WorkshopBase(SQLModel):
    date: str = Field(description="The date of the workshop in the format YYYY-MM-DD")
    cancelled: bool = Field(
        default=False, description="Whether the workshop was cancelled or not"
    )
    cancellation_reason: str | None = Field(
        default=None,
        description="The reason for the cancellation, if any",
        nullable=True,
    )


class WorkshopCreate(WorkshopBase):
    community_id: int
    # TODO somewhow this gets not resolved
    # attendance: Optional[List[AttendanceBase]]


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place with a team
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)
    team_id: int = Field(foreign_key="team.id")

    team: Team = Relationship(back_populates="workshops")
    attendances: list[Attendance] = Relationship(back_populates="workshop")
