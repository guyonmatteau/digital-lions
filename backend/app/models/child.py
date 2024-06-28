from typing import TYPE_CHECKING

from models.base import CreateProperties, MetadataColumns, UpdateProperties
from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from models.attendance import Attendance
    from models.team import Team


class ChildValidator:
    """Methods to validate child input on creation or updating."""

    @field_validator("gender")
    def validate_gender(cls, v) -> str:
        if v is not None and v not in ["male", "female"]:
            raise ValueError("Invalid gender")
        return v

    @field_validator("age")
    def validate_age(cls, v) -> int:
        if v is not None and v <= 0:
            raise ValueError("Negative age is invalid")
        return v


class ChildBase(SQLModel):
    """Base schema for child model."""

    first_name: str
    last_name: str
    age: int | None = Field(
        default=None,
        description="Age in years at the time of registration",
    )
    dob: str | None = Field(
        default=None, description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child")


class ChildRelations:
    """Relationships for child model with other tables."""

    team_id: int = Field(foreign_key="teams.id")


class Child(ChildBase, ChildRelations, MetadataColumns, table=True):
    """Schema for child model in database."""

    __tablename__ = "children"
    id: int = Field(default=None, primary_key=True)
    team: "Team" = Relationship(back_populates="children")
    attendances: list["Attendance"] = Relationship(back_populates="child")


class ChildCreate(ChildBase, ChildValidator, ChildRelations, CreateProperties):
    """Schema for creating a child."""

    pass


class ChildUpdate(SQLModel, ChildValidator, UpdateProperties):
    """Schema for updating a child."""

    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    dob: str | None = None
    gender: str | None = None
    is_active: bool | None = None
