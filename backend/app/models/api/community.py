from models.generic import CreateProperties, UpdateProperties
from pydantic import BaseModel
from sqlmodel import Field


class CommunityPostIn(BaseModel, CreateProperties):
    """API payload model for POST /communities endpoint."""

    name: str = Field(description="Name of the community")


class CommunityPatchIn(BaseModel, UpdateProperties):
    """API payload model for PATCH /communities/{id} endpoint."""

    name: str | None = None
