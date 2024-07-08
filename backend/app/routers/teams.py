import logging

import exceptions
from dependencies.services import TeamServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.out import RecordCreated, TeamOut, TeamOutBasic, WorkshopOutWithAttendance
from models.team import TeamCreate
from models.workshop import WorkshopCreate

logger = logging.getLogger()

router = APIRouter(prefix="/teams")


@router.post(
    "",
    response_model=RecordCreated,
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
    response_model=list[TeamOutBasic],
    status_code=status.HTTP_200_OK,
    summary="Get teams",
)
async def get_teams(team_service: TeamServiceDependency):
    return team_service.get_all()


@router.get(
    "/{team_id}",
    response_model=TeamOut,
    status_code=status.HTTP_200_OK,
    summary="Get team by id",
)
async def get_team(team_service: TeamServiceDependency, team_id: int):
    return team_service.get(object_id=team_id)


@router.post(
    "/{team_id}/workshops",
    status_code=status.HTTP_201_CREATED,
    summary="Add workshop to team",
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


@router.delete(
    "/{team_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a team",
)
async def delete_team(team_service: TeamServiceDependency, team_id: int, cascade: bool = False):
    try:
        return team_service.delete(object_id=team_id, cascade=cascade)
    except exceptions.TeamHasChildrenException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete team with ID {team_id} because it has related children record "
            + "and 'cascade' is set to False",
        )
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )


@router.get(
    "/{team_id}/workshops",
    status_code=status.HTTP_200_OK,
    summary="Get workshops done by team",
    # response_model=list[WorkshopOutWithAttendance],
)
async def get_workshops(team_service: TeamServiceDependency, team_id: int):
    try:
        return team_service.get_workshops(team_id)
    except exceptions.TeamNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
