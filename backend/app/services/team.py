import logging

from exceptions import CommunityNotFoundException
from models.team import TeamCreate
from repositories import ChildRepository, CommunityRepository, TeamRepository

logger = logging.getLogger(__name__)


class TeamService:
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        team_repository: TeamRepository,
        child_repository: ChildRepository,
        community_repository: CommunityRepository,
    ):
        self._team_repository = team_repository
        self._child_repository = child_repository
        self._community_repository = community_repository

    def get_teams(self):
        print("THIS")

        return self._team_repository.read_all()

    def get_team(self, team_id):
        return self._team_repository.read(object_id=team_id)

    def create_team(self, team: TeamCreate):
        """Create a new team."""
        if not self._community_repository.read(object_id=team.community_id):
            raise CommunityNotFoundException()

        for child in team.children:
            self._child_repository.create(child)

        self._team_repository.create(team)

        return self.team_repository.create_team(team)

    def create_workshop_report(self):
        """Create a report of the workshops the team has done."""
        pass

    def update_team(self, team_id, team):
        return self.team_repository.update_team(team_id, team)

    def delete_team(self, team_id):
        return self.team_repository.delete_team(team_id)
