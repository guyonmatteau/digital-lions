from typing import Annotated

from dependencies.database import SessionDependency
from dependencies.repositories import (
    AttendanceRepositoryDependency,
    ChildRepositoryDependency,
    CommunityRepositoryDependency,
    RepositoriesDependency,
    TeamRepositoryDependency,
    WorkshopRepositoryDependency,
)
from fastapi import Depends
from services import ChildService, CommunityService, TeamService


def get_team_service(
    team_repository: TeamRepositoryDependency,
    child_repository: ChildRepositoryDependency,
    community_repository: CommunityRepositoryDependency,
    workshop_repository: WorkshopRepositoryDependency,
    attendance_repository: AttendanceRepositoryDependency,
):
    return TeamService(
        team_repository=team_repository,
        child_repository=child_repository,
        community_repository=community_repository,
        workshop_repository=workshop_repository,
        attendance_repository=attendance_repository,
    )


def get_community_service(session: SessionDependency):
    return CommunityService(session=session)


def get_child_service(
    child_repository: ChildRepositoryDependency,
    team_repository: TeamRepositoryDependency,
    attendance_repository: AttendanceRepositoryDependency,
):
    return ChildService(
        child_repository=child_repository,
        team_repository=team_repository,
        attendance_repository=attendance_repository,
    )


TeamServiceDependency = Annotated[TeamService, Depends(get_team_service)]
ChildServiceDependency = Annotated[ChildService, Depends(get_child_service)]
CommunityServiceDependency = Annotated[CommunityService, Depends(get_community_service)]
