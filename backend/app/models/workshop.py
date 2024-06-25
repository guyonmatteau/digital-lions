# from models.attendance import AttendanceBase
# from models.community import Community, CommunityOut
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class WorkshopBase(SQLModel):
    date: str = Field(description="The date of the workshop in the format YYYY-MM-DD")
    cancelled: bool = Field(default=False, description="Whether the workshop was cancelled or not")
    cancellation_reason: str | None = Field(
        default=None,
        description="The reason for the cancellation, if any",
        nullable=True,
    )


class WorkshopCreate(WorkshopBase):
    # TODO somewhow this gets not resolved
    # attendance: Optional[List[AttendanceBase]]
    pass


class Workshop(WorkshopBase, table=True):
    """Data model for workshops. A workshop is a session that took place with a team
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""

    __tablename__ = "workshops"

    id: int = Field(default=None, primary_key=True)

    team_id: int = Field(foreign_key="teams.id")
    team: "Team" = Relationship(back_populates="workshops")
    attendances: list["Attendance"] = Relationship(back_populates="workshop")
