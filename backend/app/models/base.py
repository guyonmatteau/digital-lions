"""Base properties for all database models."""

from datetime import datetime

from pydantic import computed_field, field_validator


class CreatedAt:
    """Created at timestamp."""

    created_at: datetime

    @field_validator("created_at")
    def created_at(self, cls) -> datetime:
        return datetime.now()


class IsActiveProperty:
    """Is active property."""

    @field_validator("is_active")
    def is_active(self) -> bool:
        return True


class IsActiveColumn:
    """Is active column."""

    is_active: bool


class CreatedAtColumn:
    """Created at timestamp."""


class UpdatedAtProperty:
    """Updated at timestamp."""

    @computed_field
    def updated_at(self) -> datetime:
        return datetime.now()


class UpdatedAtColumn:
    """Updated at timestamp."""

    updated_at: datetime


class MetadataColumns(CreatedAtColumn, UpdatedAtColumn, IsActiveColumn):
    """Metadata columns for database models."""

    pass
