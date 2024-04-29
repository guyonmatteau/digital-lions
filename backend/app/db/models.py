from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(default= None, primary_key=True)
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
    id: int = Field(default = None, primary_key=True)
    name: str = Field()
    created_at: datetime = datetime.now()
    is_active: bool = True

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()

class Workshop(SQLModel, table=True):
    """Data model for workshops. A workshop is a session that took place
    on a given date in a given community. It can be cancelled, in that case
    there will exist a cancellation reason."""
    id: int = Field(default = None, primary_key=True)
    date: str
    cycle: int = None
    took_place: bool
    cancellation_reason: str = None

    community_id: int
    community: Community = Relationship(back_populates="workshop")

class Attendance(SQLModel, table=True):
    id: int = Field(primary_key=True)
    child_id: int = Field(foreign_key="child.id")
    attendance: str = Field()
    child_name: str
    cycle: int = None

    workshop_id: int = Field(foreign_key="workshop.id")
    workshop: Workshop = Relationship(back_populates="attendance")



class Child(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str
    last_name: str
    age: Optional[int] = Field(default=None, description="Age in years at the time of registration")
    community_id: int = Field(foreign_key="community.id")
    is_active: bool = True
    # created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    # updated_at: datetime = Field(sa_column=Column(DateTime(timezone=True), onupdate=func.now()))


