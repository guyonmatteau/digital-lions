import logging
from typing import TypeVar

from repositories.base import BaseRepository
from sqlmodel import SQLModel

logger = logging.getLogger(__name__)

Model = TypeVar("Model", bound=SQLModel)
ModelCreate = TypeVar("ModelCreate", bound=SQLModel)
ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelOut = TypeVar("ModelOut", bound=SQLModel)


class BaseService:
    """BaseService to act as a parent class for all services.
    Each service should instantiate it's own repositories, where the
    `_repository` should be the repository that the service maps to."""

    _repository: type[BaseRepository]

    def get_all(self):
        """Get all objects from the table."""
        return self._repository.read_all()

    def get(self, object_id):
        """Get an object from the table by id."""
        return self._repository.read(object_id=object_id)

    def create(self, obj: ModelCreate):
        """Create a new object on the repository."""

        return self._repository.create(obj)

    def update(self, object_id: int, obj):
        return self._repository.update(object_id=object_id, obj=obj)

    def delete(self, object_id: int):
        return self._repository.delete(object_id=object_id)
        return self._repository.delete(object_id=object_id)
