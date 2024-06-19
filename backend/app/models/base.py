"""Metadata properties for all database models."""

from datetime import datetime

from pydantic import computed_field


class CreatedAtProperty:
    """Created at timestamp."""

    @computed_field
    def created_at(self) -> datetime:
        return datetime.now()


class CreatedAtColumn:
    """Created at timestamp."""

    created_at: datetime


class IsActiveProperty:
    """Is active property, defaults to True on creation of record."""

    @computed_field
    def is_active(self) -> bool:
        return True


class IsActiveColumn:
    """Is active column."""

    is_active: bool


class LastUpdatedAtProperty:
    """Updated at timestamp."""

    @computed_field
    def last_updated_at(self) -> datetime:
        return datetime.now()


class LastUpdatedAtColumn:
    """Updated at timestamp."""

    last_updated_at: datetime


class CreateProperties(CreatedAtProperty, LastUpdatedAtProperty, IsActiveProperty):
    """Properties for create objects."""

    pass


class UpdateProperties(LastUpdatedAtProperty):
    """Metadata properties for updating models."""

    pass


class MetadataColumns(CreatedAtColumn, LastUpdatedAtColumn, IsActiveColumn):
    """Metadata columns for database models."""

    pass
