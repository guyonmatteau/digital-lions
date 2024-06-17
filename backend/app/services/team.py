from models.team import TeamBase
from repositories import ChildRepository, CommunityRepository, TeamRepository


class TeamService:
    """Team service layer to do anything related to teams."""

    def __init__(
        self,
        team_repository: TeamRepository,
        child_repository: ChildRepository,
        community_repository: CommunityRepository,
    ):
        self.team_repository = team_repository
        self.community_repository = community_repository
        self.child_repository = child_repository

    def get_teams(self):
        return self.team_repository.get_teams()

    def get_team(self, team_id):
        return self.team_repository.get_team(team_id)

    def create_team(self, team: TeamBase):
        """Create a new team."""
        if not self.community_repository.read(obj_id=team.community_id):
            raise ValueError("Community does not exist")

        # validate that the program exists (or default)

        # create children

        return self.team_repository.create_team(team)

    def create_workshop_report(self):
        """Create a report of the workshops the team has done."""
        pass

    def update_team(self, team_id, team):
        return self.team_repository.update_team(team_id, team)

    def delete_team(self, team_id):
        return self.team_repository.delete_team(team_id)
