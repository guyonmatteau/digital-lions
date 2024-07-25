import logging

import exceptions
from dependencies.services import TeamServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.api.generic import Message, RecordCreated
from models.out import TeamOut, TeamOutBasic, WorkshopOutWithAttendance
from models.team import TeamCreate
from models.workshop import WorkshopCreate

logger = logging.getLogger()

router = APIRouter(prefix="/teams")


@router.post(
    "",
    response_model=RecordCreated,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new team",
    responses={
        400: {"model": Message, "description": "Bad request"},
        409: {
            "model": Message,
            "description": "Conflict: team with name already exists",
        },
    },
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
async def get_teams(team_service: TeamServiceDependency, community_id: int = None):
    return team_service.get_all([("community_id", community_id)])


@router.get(
    "/{team_id}",
    response_model=TeamOut,
    status_code=status.HTTP_200_OK,
    summary="Get team by id",
)
async def get_team(team_service: TeamServiceDependency, team_id: int):
    try:
        return team_service.get(object_id=team_id)
    except exceptions.TeamNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.post(
    "/{team_id}/workshops",
    status_code=status.HTTP_201_CREATED,
    summary="Add workshop to team",
    response_model=RecordCreated,
    responses={
        400: {
            "model": Message,
            "description": "Bad request: missing attendance or child not in team.",
        },
        409: {"model": Message, "description": "Conflict: workshop already exists"},
        404: {
            "model": Message,
            "description": "Not found: team or child in team not found",
        },
    },
)
async def post_workshop(
    team_service: TeamServiceDependency, team_id: int, workshop: WorkshopCreate
):
    """Add a workshop to a team."""
    try:
        return team_service.create_workshop(team_id, workshop)
    except exceptions.TeamNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except exceptions.WorkshopExistsException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )
    except (
        exceptions.WorkshopIncompleteAttendance,
        exceptions.ChildNotInTeam,
        exceptions.WorkshopNumberInvalidException,
    ) as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
    except Exception as exc:
        logger.error("An error occurred: %s", str(exc))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )


@router.delete(
    "/{team_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a team",
    response_model=None,
    responses={
        404: {"model": Message, "description": "Not found"},
        409: {
            "model": Message,
            "description": "Conflict: team has children and cascade is False",
        },
    },
)
async def delete_team(team_service: TeamServiceDependency, team_id: int, cascade: bool = False):
    """Delete a team. This will delete all children if cascade is set to True.
    If you want to deactivate a team use PATCH /teams/{team_id} instead."""
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
    response_model=list[WorkshopOutWithAttendance],
)
async def get_workshops(team_service: TeamServiceDependency, team_id: int):
    try:
        return team_service.get_workshops(team_id)
    except exceptions.TeamNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with ID {team_id} not found",
        )
