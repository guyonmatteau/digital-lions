from datetime import datetime
from typing import Optional

from pydantic import field_validator, EmailStr
from sqlmodel import Field, SQLModel, AutoString

ROLES = ["admin", "partner", "community_owner", "coach"]


class UserBase(SQLModel):
    first_name: str
    last_name: str = Field(default=None)
    email_address: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    role: Optional[str] = Field(default=None, description="User role on platform")

    # @field_validator("role")
    # def validate_role(cls, value):
    #     if value not in ROLES:
    #         raise ValueError("Invalid role")


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    is_active: bool = True
    password: str = Field(default=None)


class User(UserBase, table=True):
    created_at: datetime = datetime.now()
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field(description="Password hashed by backend")

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()


class UserOut(UserBase):
    id: int
    hashed_password: str
