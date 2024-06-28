import logging

import exceptions
from models.child import ChildCreate
from repositories import ChildRepository, TeamRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class ChildService(BaseService):
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        child_repository: ChildRepository,
        team_repository: TeamRepository,
    ):
        self._repository = child_repository
        self._team_repository = team_repository

    def create(self, child: ChildCreate):
        """Create a new child."""
        try:
            self._team_repository.read(object_id=child.team_id)
        except exceptions.ItemNotFoundException:
            logger.error(f"Team with ID {child.team_id} not found")
            raise exceptions.TeamNotFoundException()
        return self._repository.create(child)
