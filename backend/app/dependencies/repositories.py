import logging
from typing import Annotated

from dependencies.database import DatabaseDependency, SessionDependency, get_session
from fastapi import Depends
from repositories import (
    AttendanceRepository,
    ChildRepository,
    CommunityRepository,
    TeamRepository,
    WorkshopRepository,
)
from sqlmodel import Session

logger = logging.getLogger(__name__)


class UnitOfWork:
    """Internal class to make each API request act as
    on a unit of work on the database."""

    def __enter__(self):
        logger.info("Starting unit of work.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """On exit rollback any staged database changes."""
        logger.info("Ending unit of work.")
        self.rollback()

    def commit(self):
        logger.info("Committing changes.")
        self._session.commit()

    def rollback(self):
        logger.error("Rolling back changes.")
        self._session.rollback()


class Repositories(UnitOfWork):
    """Container object for all repositories (i.e. all
    tables in database), which is injected into each services,
    such that they can access all tables."""

    def __init__(self, session: SessionDependency) -> None:
        """Instantiate all repositories.

        Args:
            session: database session.
        """
        self._session: SessionDependency = session
        self.community = CommunityRepository(session=self._session)


def get_repositories(session: SessionDependency) -> Repositories:
    """Callable for repositories dependency. Note this is automatically
    injecteced as context manager on each router by FastAPI."""
    return Repositories(session=session)


RepositoriesDependency = Annotated[Repositories, Depends(get_repositories)]


def get_team_repository(session: SessionDependency):
    return TeamRepository(session=session)


def get_community_repository(session: SessionDependency):
    return CommunityRepository(session=session)


def get_child_repository(session: SessionDependency):
    return ChildRepository(session=session)


def get_workshop_repository(session: SessionDependency):
    return WorkshopRepository(session=session)


def get_attendance_repository(session: SessionDependency):
    return AttendanceRepository(session=session)


AttendanceRepositoryDependency = Annotated[
    AttendanceRepository, Depends(get_attendance_repository)
]
CommunityRepositoryDependency = Annotated[CommunityRepository, Depends(get_community_repository)]
ChildRepositoryDependency = Annotated[ChildRepository, Depends(get_child_repository)]
TeamRepositoryDependency = Annotated[TeamRepository, Depends(get_team_repository)]
WorkshopRepositoryDependency = Annotated[WorkshopRepository, Depends(get_workshop_repository)]
