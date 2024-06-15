from typing import Annotated

from dependencies.database import DatabaseDependency
from fastapi import Depends
from repositories.team import TeamRepository

# from repositories.community import CommunityRepository
from repositories.base import BaseRepository
from models.community import Community


def get_team_repository(db: DatabaseDependency):
    return TeamRepository(db=db)


# class CommunityRepository([Community]):
#     pass


def get_community_repository(db: DatabaseDependency):
    return BaseRepository(model=Community, db=db)


TeamRepositoryDependency = Annotated[TeamRepository, Depends(get_team_repository)]
CommunityRepositoryDependency = Annotated[BaseRepository, Depends(get_community_repository)]
