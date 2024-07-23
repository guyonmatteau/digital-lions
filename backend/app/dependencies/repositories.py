import logging

from dependencies.database import SessionDependency
from repositories import (
    AttendanceRepository,
    ChildRepository,
    CommunityRepository,
    TeamRepository,
    WorkshopRepository,
)
from repositories.base import Columns

logger = logging.getLogger(__name__)


class UnitOfWork:
    """Internal class to make each API request act as
    on a unit of work on the database."""

    attendances: AttendanceRepository
    children: ChildRepository
    communities: CommunityRepository
    teams: TeamRepository
    workshops: WorkshopRepository

    cols = Columns

    def __init__(self, session: SessionDependency) -> None:
        """Instantiate all repositories.

        Args:
            session: database session.
        """
        self._session: SessionDependency = session
        self._attendances = AttendanceRepository(session=self._session)
        self._communities = CommunityRepository(session=self._session)
        self._children = ChildRepository(session=self._session)
        self._teams = TeamRepository(session=self._session)
        self._workshops = WorkshopRepository(session=self._session)

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
