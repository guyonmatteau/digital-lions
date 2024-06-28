from typing import Annotated

from dependencies.repositories import (
    ChildRepositoryDependency,
    CommunityRepositoryDependency,
    TeamRepositoryDependency,
)
from fastapi import Depends
from services.child import ChildService
from services.community import CommunityService
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


def get_community_service(community_repository: CommunityRepositoryDependency):
    return CommunityService(community_repository=community_repository)


def get_child_service(
    child_repository: ChildRepositoryDependency, team_repository: TeamRepositoryDependency
):
    return ChildService(child_repository=child_repository, team_repository=team_repository)


TeamServiceDependency = Annotated[TeamService, Depends(get_team_service)]
ChildServiceDependency = Annotated[ChildService, Depends(get_child_service)]
CommunityServiceDependency = Annotated[CommunityService, Depends(
    get_community_service)]
