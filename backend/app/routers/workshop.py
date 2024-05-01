from typing import Optional

from db.models import Workshop
from db.session import get_db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

router = APIRouter(prefix="/workshop")

@router.post("", summary="Add workshop to database.", status_code=status.HTTP_201_CREATED, response_model=Workshop)
async def add_workshop(workshop: Workshop, db: Session = Depends(get_db)):
    db.add(workshop)
    db.commit()
    db.refresh(workshop)
    return workshop




@router.get("", summary="Get list of workshops", status_code=status.HTTP_200_OK, response_model=Optional[list[Workshop]])
async def get_workshops(workshop_id: Optional[int] = None, community_id: Optional[int] = None, date: Optional[str] = None, db: Session = Depends(get_db)):
    """Get the Workshop of a child to a workshop.
    If the id is not provided, it will return all the Workshops."""
    filters = []
    if workshop_id is not None:
        filters.append(Workshop.id == workshop_id)
    if community_id is not None:
        filters.append(Workshop.community_id == community_id)
    Workshops = db.query(Workshop).filter(*filters).all()
    return Workshops

