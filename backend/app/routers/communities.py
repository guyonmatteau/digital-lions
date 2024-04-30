from typing import Optional

from db.models import Community
from db.session import get_db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlmodel import Field, Session, SQLModel, create_engine, select

router = APIRouter(prefix="/communities")


@router.get(
    "",
    summary="Get communities",
    status_code=status.HTTP_200_OK,
    response_model=Optional[list[Community]],
)
async def get_communities(db: Session = Depends(get_db)):
    communities = db.query(Community).all()
    return communities


@router.post(
    "",
    summary="Add a community",
    status_code=status.HTTP_201_CREATED,
    response_model=Community,
)
async def add_community(community: Community, db: Session = Depends(get_db)):
    if db.query(Community).filter(Community.name == community.name).first():
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": f"There already exists a community with name {community.name}"
            },
        )
    db.add(community)
    db.commit()
    db.refresh(community)
    return community


@router.put(
    "/{community_id}",
    summary="Update a community",
    response_model=Community,
    status_code=status.HTTP_200_OK,
)
async def update_community(
    community_id: int, community: Community, db: Session = Depends(get_db)
):
    db_community = db.get(Community, community_id)
    if not db_community:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"Community with ID {community_id} not found"},
        )
    community_data = community.model_dump(exclude_unset=True)
    db_community.sqlmodel_update(community_data)
    db.add(db_community)
    db.commit()
    db.refresh(db_community)
    return db_community
