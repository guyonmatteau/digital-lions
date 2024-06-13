from __future__ import annotations

from datetime import datetime

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class ChildBase(SQLModel):
    """Base schema for child model."""

    first_name: str
    last_name: str
    age: int | None = Field(
        default=None, description="Age in years at the time of registration",
    )
    dob: str | None = Field(default=None,
                            description="Date of birth in the format YYYY-MM-DD")
    gender: str | None = Field(default=None, description="Gender of child")


class ChildCreate(ChildBase):
    """Schema for creating a child."""

    community_id: int = Field(foreign_key="community.id")


class ChildUpdate(ChildCreate):
    """Schema for updating a child."""

    is_active: bool = True

    @field_validator("gender")
    def validate_gender(cls, v) -> str:
        if v is not None and v not in ["male", "female"]:
            raise ValueError("Invalid gender")
        return v


    @field_validator("age")
    def validate_age(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Negative age is invalid")
        return v


class Child(ChildUpdate, table=True):
    """Schema for child model in database."""

    __table_args__ = {"extend_existing": True}
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = datetime.now()
    is_active: bool = True

    community: Community | None = Relationship(back_populates="children")
    attendances: list[Attendance] = Relationship(back_populates="child")
