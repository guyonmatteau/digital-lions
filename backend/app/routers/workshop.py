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
async def get_workshops(community_id: Optional[int] = None, date: Optional[str] = None, db: Session = Depends(get_db)):
    """Get the Workshop of a child to a workshop.
    If the id is not provided, it will return all the Workshops."""
    if id:
        Workshop = db.get(Workshop, id)
        if not Workshop:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": f"Workshop with id {id} not found"},
            )
        return Workshop

    filters = []
    if child_id is not None:
        filters.append(Child.id == child_id)
    Workshops = db.query(Workshops).filter(*filters).all()
    return Workshops

