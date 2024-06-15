import logging
from typing import Annotated

from dependencies.services import get_team_service
from exceptions import (
    ItemAlreadyExistsException,
)
from fastapi import APIRouter, Depends, HTTPException, status
from models.team import TeamBase
from services.team import TeamService

logger = logging.getLogger()

router = APIRouter(prefix="/teams", tags=["teams"])


@router.post(
    "",
    response_model=TeamBase,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new team",
)
async def post_team(
    team_service: Annotated[TeamService, Depends(get_team_service)], team: TeamBase
):
    try:
        await team_service.create_team(team)
    except ItemAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Team with name {team.name} already exists",
        )
