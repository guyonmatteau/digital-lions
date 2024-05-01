from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel
from pydantic import field_validator


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password: str
    email_address: str
    role: str = None
    is_active: bool = True
    created_at: datetime = datetime.now()

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()


class Community(SQLModel, table=True):
    """Community model."""
    id: int = Field(default=None, primary_key=True)
    name: str = Field()
    created_at: datetime = datetime.now()
    is_active: bool = True
    
    workshops: list["Workshop"] = Relationship(back_populates="community")

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()


class Child(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: Optional[int] = Field(
        default=None, description="Age in years at the time of registration"
    )
    created_at: datetime = datetime.now()
    is_active: bool = True

    community_id: int = Field(foreign_key="community.id")
    # updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), onupdate=func.now()))

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
    community: Community = Relationship(back_populates="workshops")


class Attendance(SQLModel, table=True):
    """Data model for attenadance of a child in a workshop."""
    id: int = Field(primary_key=True)
    child_id: int = Field(foreign_key="child.id")
    workshop_id: int = Field(foreign_key="workshop.id")
    attendance: str 
    
    @field_validator("attendance")
    def validate_attendance(cls, v):
        if v not in ["present", "absent", "cancelled"]:
            raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
        return v

    # workshop: Workshop = Relationship(back_populates="attendance")



