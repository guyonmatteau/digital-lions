"""FastAPI dependencies to be injected into route handlers."""

from typing import Annotated

from database.session import SessionDependency
from fastapi import Depends
from services import ChildService, CommunityService, TeamService


def get_team_service(session: SessionDependency):
    return TeamService(session=session)


def get_community_service(session: SessionDependency):
    return CommunityService(session=session)


def get_child_service(session: SessionDependency):
    return ChildService(session=session)


TeamServiceDependency = Annotated[TeamService, Depends(get_team_service)]
ChildServiceDependency = Annotated[ChildService, Depends(get_child_service)]
CommunityServiceDependency = Annotated[CommunityService, Depends(get_community_service)]
