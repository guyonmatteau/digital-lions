from datetime import datetime

from pydantic import BaseModel, computed_field


class Message(BaseModel):
    """Generic API message response model for API error messages."""

    detail: str


class RecordCreated(BaseModel):
    """Generic API message response model for
    when an object created in the database."""

    id: int


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


class IsActiveUpdateProperty:
    """Is active property, defaults to True on creation of record,
    but can be updated to false at a later stage."""

    is_active: bool | None = None


class IsActiveColumn:
    """Is active column in databases table."""

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


class UpdateProperties(LastUpdatedAtProperty, IsActiveUpdateProperty):
    """Metadata properties for updating models."""

    pass


class MetadataColumns(CreatedAtColumn, LastUpdatedAtColumn, IsActiveColumn):
    """Metadata columns for database models."""

    pass
