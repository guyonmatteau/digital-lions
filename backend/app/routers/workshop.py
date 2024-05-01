from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from db.session import get_db
from models.community import Community
from models.workshop import Workshop

router = APIRouter(prefix="/workshop")


@router.post(
    "",
    summary="Add workshop",
    status_code=status.HTTP_201_CREATED,
    response_model=Workshop,
)
async def add_workshop(workshop: Workshop, db: Session = Depends(get_db)):
    if not db.query(Community).filter(Community.id == workshop.community_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {workshop.community_id} not found",
        )
    db.add(workshop)
    db.commit()
    db.refresh(workshop)
    return workshop

@router.get("/{workshop_id}", summary="Get workshop by ID", response_model=Workshop)
async def get_workshop(workshop_id: int, db: Session = Depends(get_db)):
    workshop = db.get(Workshop, workshop_id)
    if workshop is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workshop with ID {workshop_id} not found",
        )
    return workshop


@router.get(
    "",
    summary="Get workshops",
    status_code=status.HTTP_200_OK,
    response_model=Optional[list[Workshop]],
)
async def get_workshops(
    community_id: Optional[int] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Get the Workshop of a child to a workshop."""
    filters = []
    if community_id is not None:
        filters.append(Workshop.community_id == community_id)
    if date is not None:
        filters.append(Workshop.date == date)
    workshops = db.query(Workshop).filter(*filters).all()
    return workshops
