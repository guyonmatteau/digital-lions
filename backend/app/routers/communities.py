import logging

import exceptions
from dependencies.repositories import RepositoriesDependency
from dependencies.services import CommunityServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.community import CommunityCreate, CommunityUpdate
from models.out import CommunityOutBasic

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOutBasic,
    status_code=status.HTTP_200_OK,
    summary="Get community by ID",
)
async def get_community(community_id: int, repositories: RepositoriesDependency):
    """Get a community by ID."""
    try:
        return repositories.community.read(community_id)
    except exceptions.CommunityNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found",
        )


@router.get(
    "",
    summary="Get communities",
    status_code=status.HTTP_200_OK,
    response_model=list[CommunityOutBasic] | None,
)
async def get_communities(service: CommunityServiceDependency):
    return service.get_all()


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=CommunityOutBasic,
)
async def add_community(community: CommunityCreate, repositories: RepositoriesDependency):
    """Add a community."""
    try:
        community = repositories.community.create(community)
        repositories.commit()
        return community
    except exceptions.CommunityAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Community with name {community.name} already exists.",
        )


@router.patch(
    "/{community_id}",
    summary="Update a community",
    response_model=CommunityOutBasic,
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
