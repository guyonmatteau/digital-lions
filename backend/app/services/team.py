import logging

from exceptions import CommunityNotFoundException
from models.team import TeamCreate
from repositories import ChildRepository, CommunityRepository, TeamRepository
from services.base import BaseService

logger = logging.getLogger(__name__)


class TeamService(BaseService):
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        team_repository: TeamRepository,
        child_repository: ChildRepository,
        community_repository: CommunityRepository,
    ):
        self._repository = team_repository
        self._child_repository = child_repository
        self._community_repository = community_repository

    def create(self, team: TeamCreate):
        """Create a new team."""
        if not self._community_repository.read(object_id=team.community_id):
            raise CommunityNotFoundException()

        return self._repository.create(team)

    def create_workshop_report(self):
        """Create a report of the workshops the team has done."""
        pass
