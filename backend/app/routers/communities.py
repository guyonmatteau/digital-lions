from typing import Optional

from dependencies.repositories import CommunityRepositoryDependency
from dependencies.database import DatabaseDependency
from fastapi import APIRouter, Depends, HTTPException, status
from models.community import Community, CommunityCreate
from models.out import CommunityOut

router = APIRouter(prefix="/communities")


@router.get(
    "/{community_id}",
    response_model=CommunityOut,
    status_code=status.HTTP_200_OK,
    summary="Get a community",
)
async def get_community(community_id: int, repository=CommunityRepositoryDependency):
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
    response_model=list[Community] | None,
)
async def get_communities(database: DatabaseDependency):
    return database.query(Community).all()
    # return repository.read_all()


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=Community,
)
async def add_community(community: CommunityCreate, repository=CommunityRepositoryDependency):
    if db.query(Community).filter(Community.name == community.name).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"There already exists a community with name {community.name}",
        )
    new_community = Community(**community.dict())
    db.add(new_community)
    db.commit()
    db.refresh(new_community)
    return new_community


@router.patch(
    "/{community_id}",
    summary="Update a community",
    response_model=Community,
    status_code=status.HTTP_200_OK,
)
async def update_community(
    community_id: int, community: Community, repository=CommunityRepositoryDependency
):
    db_community = db.get(Community, community_id)
    if not db_community:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {community_id} not found",
        )
    community_data = community.model_dump(exclude_unset=True)
    db_community.sqlmodel_update(community_data)
    db.add(db_community)
    db.commit()
    db.refresh(db_community)
    return db_community
