import logging

import exceptions
from dependencies.services import TeamServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.out import TeamOut
from models.team import TeamBase, TeamCreate
from models.workshop import WorkshopCreate

logger = logging.getLogger()

router = APIRouter(prefix="/teams", tags=["teams"])


@router.post(
    "",
    response_model=TeamBase,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new team",
)
async def post_team(team_service: TeamServiceDependency, team: TeamCreate):
    try:
        return team_service.create(team)
    except exceptions.CommunityNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Community with ID {team.community_id} not found",
        )
    except exceptions.ItemAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Team with name {team.name} already exists",
        )


@router.get(
    "",
    response_model=list[TeamOut],
    status_code=status.HTTP_200_OK,
    summary="Get all teams",
)
async def get_teams(team_service: TeamServiceDependency):
    return team_service.get_all()


@router.get(
    "/{team_id}",
    response_model=TeamOut,
    status_code=status.HTTP_200_OK,
    summary="Get a teams",
)
async def get_team(team_service: TeamServiceDependency, team_id: int):
    return team_service.get(object_id=team_id)


@router.post(
    "/{team_id}/workshops",
    status_code=status.HTTP_201_CREATED,
    summary="Add a workshop to a team",
)
async def create_workshop(
    team_service: TeamServiceDependency, team_id: int, workshop: WorkshopCreate
):
    try:
        return team_service.create_workshop(team_id, workshop)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
