from datetime import datetime

from pydantic import field_validator
from sqlmodel import Field, SQLModel

ROLES = ["admin", "maintainer", "coach"]

class UserBase(SQLModel):
    username: str
    email_address: str
    role: str | None = None

    @field_validator("role")
    def validate_role(cls, value):
        if value not in ROLES:
            raise ValueError("Invalid role")

class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    is_active: bool = True

class User(UserUpdate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = datetime.now()

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()

class UserOut(UserBase):
    id: int
