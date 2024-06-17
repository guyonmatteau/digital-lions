import logging

from dependencies.repositories import CommunityRepositoryDependency
from fastapi import APIRouter, HTTPException, status
from models.community import Community, CommunityCreate
from models.out import CommunityOut

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOut,
    status_code=status.HTTP_200_OK,
    summary="Get a community",
)
async def get_community(community_id: int, repository: CommunityRepositoryDependency):
    community = repository.read(community_id)
    if not community:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found",
        )
    return community


@router.get(
    "",
    summary="Get communities",
    status_code=status.HTTP_200_OK,
    response_model=list[CommunityOut] | None,
)
async def get_communities(repository: CommunityRepositoryDependency):
    return repository.read_all()


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=CommunityOut,
)
async def add_community(community: CommunityCreate, repository: CommunityRepositoryDependency):
    try:
        # TODO repositrory will be intermediated by service
        return repository.create(community)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"There already exists a community with name {community.name}",
        )


@router.patch(
    "/{community_id}",
    summary="Update a community",
    response_model=Community,
    status_code=status.HTTP_200_OK,
)
async def update_community(
    community_id: int, community: Community, repository: CommunityRepositoryDependency
):
    try:
        return repository.update(community_id, community)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bad request")
