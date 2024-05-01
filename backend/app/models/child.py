from datetime import datetime
from typing import List, Optional

from pydantic import field_validator
from sqlmodel import Field, Relationship, SQLModel


class ChildCreate(SQLModel):
    first_name: str
    last_name: str
    age: Optional[int] = Field(
        default=None, description="Age in years at the time of registration"
    )
    community_id: int = Field(foreign_key="community.id")
    community: ["community"] = Relationship(back_populates="children")
    
    @field_validator("age")
    def validate_age(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Negative age is invalid")
        return v    


class Child(ChildCreate, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = datetime.now()
    is_active: bool = True


# class ChildOutWithCommunity(Child):
    # community: Community = None
