import logging

import exceptions
from dependencies.services import CommunityServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.community import CommunityCreate, CommunityUpdate
from models.out import CommunityOut

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOut,
    status_code=status.HTTP_200_OK,
    summary="Get community by ID",
)
async def get_community(community_id: int, service: CommunityServiceDependency):
    """Get a community by ID."""
    try:
        return service.get(community_id)
    except exceptions.CommunityNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found",
        )


@router.get(
    "",
    summary="Get communities",
    status_code=status.HTTP_200_OK,
    response_model=list[CommunityOut] | None,
)
async def get_communities(service: CommunityServiceDependency):
    return service.get_all()


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=CommunityOut,
)
async def add_community(community: CommunityCreate, service: CommunityServiceDependency):
    """Add a community."""
    try:
        return service.create(community)
    except exceptions.CommunityAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Community with name {community.name} already exists.",
        )


@router.patch(
    "/{community_id}",
    summary="Update a community",
    response_model=CommunityOut,
    status_code=status.HTTP_200_OK,
)
async def update_community(
    community_id: int, community: CommunityUpdate, service: CommunityServiceDependency
):
    """Update a community."""
    try:
        return service.update(community_id, community)
    except exceptions.CommunityNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found.",
        )
