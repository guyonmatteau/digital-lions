import logging
from typing import TypeVar

import repositories
from dependencies.database import SessionDependency
from repositories.base import Columns
from sqlmodel import SQLModel

Model = TypeVar("Model", bound=SQLModel)
ModelCreate = TypeVar("ModelCreate", bound=SQLModel)
ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelOut = TypeVar("ModelOut", bound=SQLModel)


logger = logging.getLogger(__name__)


class BaseService:
    """Internal class to make each API request act as
    on a unit of work on the database."""

    attendances: repositories.AttendanceRepository
    children: repositories.ChildRepository
    communities: repositories.CommunityRepository
    teams: repositories.TeamRepository
    workshops: repositories.WorkshopRepository

    cols = Columns

    def __init__(self, session: SessionDependency) -> None:
        """Instantiate all repositories.

        Args:
            session: database session.
        """
        self._session: SessionDependency = session
        self._attendances = repositories.AttendanceRepository(session=self._session)
        self._communities = repositories.CommunityRepository(session=self._session)
        self._children = repositories.ChildRepository(session=self._session)
        self._teams = repositories.TeamRepository(session=self._session)
        self._workshops = repositories.WorkshopRepository(session=self._session)

        self._cols = Columns

    def __enter__(self):
        """On entering context start a transaction."""
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """On exit rollback any staged database changes."""
        self.rollback()

    def commit(self) -> None:
        """Commit all staged changes to the database."""
        self._session.commit()

    def rollback(self) -> None:
        """Rollback all staged changes in the database."""
        self._session.rollback()


# class BaseService:
#     """BaseService to act as a parent class for all services.
#     Each service should instantiate it's own repositories, where the
#     `_repository` should be the repository that the service maps to."""
#
#     _repository: type[BaseRepository]
#     cols: Columns
#
#     def get_all(self):
#         """Get all objects from the table."""
#         return self._repository.read_all()
#
#     def get(self, object_id):
#         """Get an object from the table by id."""
#         return self._repository.read(object_id=object_id)
#
#     def create(self, obj: ModelCreate):
#         """Create a new object on the repository."""
#         return self._repository.create(obj)
#
#     def update(self, object_id: int, obj):
#         return self._repository.update(object_id=object_id, obj=obj)
#
#     def delete(self, object_id: int):
#         return self._repository.delete(object_id=object_id)
