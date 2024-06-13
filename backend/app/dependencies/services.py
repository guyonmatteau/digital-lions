from typing import Annotated

from dependencies.repositories import get_team_repository
from fastapi import Depends
from repositories.team import TeamRepository
from services.team import TeamService


def get_team_service(
    team_repository: Annotated[TeamRepository, Depends(get_team_repository)]
):
    return TeamService(team_repository=team_repository)
