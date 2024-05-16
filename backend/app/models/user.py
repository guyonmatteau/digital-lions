from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator
from sqlmodel import AutoString, Field, SQLModel

ROLES = ["admin", "partner", "community_owner", "coach"]


class UserLogin(BaseModel):
    email_address: EmailStr
    password: str


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
    hashed_password: bytes = Field(description="Hashed password in bytes")
    salt: bytes = Field(
        description="Random byte string with which the password is encrypted"
    )

    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()


class UserOut(UserBase):
    id: int
