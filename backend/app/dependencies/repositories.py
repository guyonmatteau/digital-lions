from typing import Annotated

from dependencies.database import DatabaseDependency
from fastapi import Depends
from repositories import ChildRepository, CommunityRepository, TeamRepository


def get_team_repository(db: DatabaseDependency):
    return TeamRepository(db=db)


def get_community_repository(db: DatabaseDependency):
    return CommunityRepository(db=db)


def get_child_repository(db: DatabaseDependency):
    return ChildRepository(db=db)


CommunityRepositoryDependency = Annotated[
    CommunityRepository, Depends(get_community_repository)
]
ChildRepositoryDependency = Annotated[ChildRepository, Depends(get_child_repository)]
TeamRepositoryDependency = Annotated[TeamRepository, Depends(get_team_repository)]
