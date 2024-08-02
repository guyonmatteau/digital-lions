import logging

import exceptions
from dependencies.services import CommunityServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.api.community import CommunityPatchIn, CommunityPostIn
from models.api.generic import RecordCreated
from models.out import CommunityOutBasic, CommunityOutGetById

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOutGetById,
    status_code=status.HTTP_200_OK,
    summary="Get community by ID",
)
async def get_community(community_id: int, service: CommunityServiceDependency):
    """Get a community by ID."""
    try:
        return service.get(community_id)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found",
        )


@router.get(
    "",
    summary="List all communities",
    status_code=status.HTTP_200_OK,
    response_model=list[CommunityOutBasic] | None,
)
async def get_communities(service: CommunityServiceDependency):
    return service.get_all()


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=RecordCreated,
)
async def post_community(community: CommunityPostIn, service: CommunityServiceDependency):
    """Add a community."""
    try:
        return service.create(community)
    except exceptions.CommunityAlreadyExistsException as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error.",
        )


@router.patch(
    "/{community_id}",
    summary="Update a community",
    response_model=CommunityOutGetById,
    status_code=status.HTTP_200_OK,
)
async def update_community(
    community_id: int, community: CommunityPatchIn, service: CommunityServiceDependency
):
    """Update a community."""
    try:
        return service.update(community_id, community)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found.",
        )
