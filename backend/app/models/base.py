"""Base properties for all database models."""

from datetime import datetime

from pydantic import computed_field


class CreatedAt:
    """Created at timestamp."""

    @computed_field
    def created_at(self) -> datetime:
        return datetime.now()

    def is_active(self) -> bool:
        return True


class UpdatedAt:
    """Updated at timestamp."""

    @computed_field
    def updated_at(self) -> datetime:
        return datetime.now()
