from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from db.session import get_db
from sqlalchemy.orm import Session
from db.models import Community
from typing import Optional


router = APIRouter(prefix="/communities")


@router.get("", summary="Get communities")
async def get_communities(db: Session = Depends(get_db)):
    communities = db.query(Community).all()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"communities": [community.as_dict() for community in communities]},
    )


@router.post("", summary="Add a community")
async def add_community(community: Community, db: Session = Depends(get_db)):
    if (
        db.query(Community)
        .filter(Community.name == community.name)
        .first()
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "There already exists a community with the same name."},
        )

    new_community = Community(**community.dict())
    db.add(new_community)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=new_community.as_dict(),
    )


@router.put("/{community_id}", summary="Update a community")
async def update_community(
    community_id: int, community: Community, db: Session = Depends(get_db)
):
    db_community = (
        db.query(Community).filter(Community.id == community_id).first()
    )
    if db_community is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "community not found"},
        )

    for key, value in community.dict().items():
        setattr(db_community, key, value)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=db_community.as_dict(),
    )
