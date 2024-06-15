from typing import Annotated

from dependencies.repositories import TeamRepositoryDependency
from fastapi import Depends
from services.team import TeamService


def get_team_service(team_repository: TeamRepositoryDependency):
    return TeamService(team_repository=team_repository)


TeamServiceDependency = Annotated[TeamService, Depends(get_team_service)]
