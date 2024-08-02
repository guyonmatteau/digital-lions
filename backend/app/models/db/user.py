from models.base import MetadataColumns
from pydantic import EmailStr
from sqlmodel import AutoString, Field, SQLModel


class User(SQLModel, MetadataColumns, table=True):
    """User model in database."""

    __tablename__ = "users"
    first_name: str
    last_name: str = Field(default=None)
    email_address: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    role: str | None = Field(default=None, description="User role on platform")

    id: int | None = Field(default=None, primary_key=True)
    hashed_password: bytes = Field(description="Hashed password in bytes")
    salt: bytes = Field(description="Random byte string with which the password is encrypted")
