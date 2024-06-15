from typing import Annotated

from dependencies.database import DatabaseDependency
from fastapi import Depends
from repositories.child import ChildRepository

# from repositories.team import TeamRepository
from repositories.community import CommunityRepository


def get_team_repository(db: DatabaseDependency):
    return TeamRepository(db=db)


# class CommunityRepository([Community]):
#     pass


def get_community_repository(db: DatabaseDependency):
    return CommunityRepository(db=db)

def get_child_repository(db: DatabaseDependency):
    return ChildRepository(db=db)



# TeamRepositoryDependency = Annotated[TeamRepository, Depends(get_team_repository)]
CommunityRepositoryDependency = Annotated[CommunityRepository, Depends(get_community_repository)]
ChildRepositoryDependency = Annotated[ChildRepository, Depends(get_child_repository)]
