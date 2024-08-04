from models.generic import CreateProperties, MetadataColumns, UpdateProperties
from pydantic import BaseModel
from sqlmodel import Field


class CommunityPostIn(BaseModel, CreateProperties):
    """API payload model for POST /communities endpoint."""

    name: str = Field(description="Name of the community")


class CommunityPatchIn(BaseModel, UpdateProperties):
    """API payload model for PATCH /communities/{id} endpoint."""

    name: str | None = None


class CommunityGetOut(BaseModel):
    """API response model for GET /communities."""

    id: int
    name: str


class CommunityGetByIdOut(BaseModel, MetadataColumns):
    """API response model for GET /communities/:id."""

    id: int
    name: str
