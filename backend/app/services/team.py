from app.models.team import TeamCreate
from app.repositories.team import TeamRepository


class TeamService:
    """Team service layer to do anything related to teams."""

    def __init__(self, team_repository: TeamRepository):
        self.repository = team_repository

    def get_teams(self):
        return self.repository.get_teams()

    def get_team(self, team_id):
        return self.repository.get_team(team_id)

    def create_team(self, team: TeamCreate):
        """Create a new team."""

        # validate the community exists
        #
        # validate that the program exists (or default)

        # create children

        return self.repository.create_team(team)

    def create_workshop_report(self, team_id):
        """Create a report of the workshops the team has done."""

        # create

        return self.repository.create_workshop_report(team_id)

    def update_team(self, team_id, team):
        return self.repository.update_team(team_id, team)

    def delete_team(self, team_id):
        return self.repository.delete_team(team_id)
