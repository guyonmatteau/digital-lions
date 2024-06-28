import logging

import exceptions
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
        try:
            self._community_repository.read(object_id=team.community_id)
        except exceptions.ItemNotFoundException:
            raise exceptions.CommunityNotFoundException()

        # first create the team, then add children to it
        children = team.children
        delattr(team, "children")
        new_team = self._repository.create(team)

        for child in children:
            child.team_id = new_team.id
            self._child_repository.create(child)
        return new_team

    def create_workshop_report(self):
        """Create a report of the workshops the team has done."""
        pass
