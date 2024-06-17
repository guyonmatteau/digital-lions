from typing import Annotated

from dependencies.repositories import (
    ChildRepositoryDependency,
    CommunityRepositoryDependency,
    TeamRepositoryDependency,
)
from fastapi import Depends
from services.team import TeamService


def get_team_service(
    team_repository: TeamRepositoryDependency,
    child_repository: ChildRepositoryDependency,
    community_repository: CommunityRepositoryDependency,
):
    return TeamService(
        team_repository=team_repository,
        child_repository=child_repository,
        community_repository=community_repository,
    )


TeamServiceDependency = Annotated[TeamService, Depends(get_team_service)]
