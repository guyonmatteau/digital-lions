import logging

from dependencies.services import CommunityServiceDependency
from exceptions import CommunityAlreadyExistsException, CommunityNotFoundException
from fastapi import APIRouter, HTTPException, status
from models.community import CommunityCreate, CommunityUpdate
from models.out import CommunityOut

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOut,
    status_code=status.HTTP_200_OK,
    summary="Get a community",
)
async def get_community(community_id: int, service: CommunityServiceDependency):
    try:
        return service.get(community_id)
    except CommunityNotFoundException:
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
    try:
        return service.create(community)
    except CommunityAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"There already exists a community with name {community.name}",
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
    try:
        return service.update(community_id, community)
    except CommunityNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found.",
        )
