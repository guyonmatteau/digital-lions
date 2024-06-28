from typing import Annotated

from dependencies.database import DatabaseDependency
from fastapi import Depends
from repositories import (
    AttendanceRepository,
    ChildRepository,
    CommunityRepository,
    TeamRepository,
    WorkshopRepository,
)


def get_team_repository(db: DatabaseDependency):
    return TeamRepository(db=db)


def get_community_repository(db: DatabaseDependency):
    return CommunityRepository(db=db)


def get_child_repository(db: DatabaseDependency):
    return ChildRepository(db=db)


def get_workshop_repository(db: DatabaseDependency):
    return WorkshopRepository(db=db)


def get_attendance_repository(db: DatabaseDependency):
    return AttendanceRepository(db=db)


AttendanceRepositoryDependency = Annotated[
    AttendanceRepository, Depends(get_attendance_repository)
]
CommunityRepositoryDependency = Annotated[CommunityRepository, Depends(
    get_community_repository)]
ChildRepositoryDependency = Annotated[ChildRepository, Depends(
    get_child_repository)]
TeamRepositoryDependency = Annotated[TeamRepository, Depends(
    get_team_repository)]
WorkshopRepositoryDependency = Annotated[WorkshopRepository, Depends(
    get_workshop_repository)]
