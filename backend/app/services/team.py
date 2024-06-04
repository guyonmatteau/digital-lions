# class TeamService:
#     def __init__(self, team_repository: TeamRepository):
#         self.team_repository = team_repository
#
#     async def get_teams(self):
#         return self.team_repository.get_teams()
#
#     async def get_team(self, team_id):
#         return self.team_repository.get_team(team_id)
#
#     def create_team(self, team):
#         return self.team_repository.create_team(team)
#
#     def update_team(self, team_id, team):
#         return self.team_repository.update_team(team_id, team)
#     def delete_team(self, team_id):
#         return self.team_repository.delete_team(team_id)
