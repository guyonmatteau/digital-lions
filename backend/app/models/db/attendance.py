from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.child import Child
    from models.workshop import Workshop


class Attendance(SQLModel, table=True):
    """Data model for attendance of a child in a workshop."""

    __tablename__ = "attendances"

    id: int = Field(default=None, primary_key=True)
    attendance: str

    child_id: int = Field(
        sa_column=Column(Integer, ForeignKey("children.id", ondelete="CASCADE")),
    )
    workshop_id: int = Field(
        sa_column=Column(Integer, ForeignKey("workshops.id", ondelete="CASCADE")),
    )

    child: "Child" = Relationship(back_populates="attendances")
    workshop: "Workshop" = Relationship(back_populates="attendance")
