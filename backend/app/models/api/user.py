from models.api.generic import CreateProperties, UpdateProperties
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
    role: str | None = Field(default=None, description="User role on platform")

    @field_validator("role")
    def validate_role(cls, value):
        if value not in ROLES:
            raise ValueError("Invalid role")


class UserCreate(UserBase, CreateProperties):
    password: str


class UserUpdate(UserBase, UpdateProperties):
    first_name: str | None = None
    last_name: str | None = None
    email_address: EmailStr | None = None
    role: str | None = None
    password: str | None = None
