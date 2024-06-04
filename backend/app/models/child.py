from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.models.base import ChildBase
from app.models.community import Community


class ChildCreate(ChildBase):
    """Schema for creating a child."""

    community_id: int = Field(foreign_key="community.id")


class ChildUpdate(ChildCreate):
    """Schema for updating a child."""

    is_active: bool = True

    # @field_validator("age")
    # def validate_age(cls, v):
    # if v is not None and v <= 0:
    # raise ValueError("Negative age is invalid")
    # return v


class Child(ChildUpdate, table=True):
    """Schema for child model in database."""

    id: int = Field(default=None, primary_key=True)
    created_at: datetime = datetime.now()
    is_active: bool = True

    community: Community | None = Relationship(back_populates="children")
    attendances: list["Attendance"] = Relationship(back_populates="child")
