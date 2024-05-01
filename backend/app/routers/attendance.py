from typing import Optional

from db.models import Attendance
from db.session import get_db
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

router = APIRouter(prefix="/attendance")


@router.post("", summary="Add attendance of child to a workshop", status_code=status.HTTP_201_CREATED, response_model=Attendance)
async def add_attendances(attendance: Attendance, db: Session = Depends(get_db)):
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance



@router.get("", summary="Get attendances of children to workshops", status_code=status.HTTP_200_OK, response_model=Optional[list[Attendance]])
async def get_attendances(id: Optional[int] = None, child_id: Optional[int] = None, db: Session = Depends(get_db)):
    """Get the attendance of a child to a workshop.
    If the id is not provided, it will return all the attendances."""
    if id:
        attendance = db.get(Attendance, id)
        if not attendance:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": f"Attendance with id {id} not found"},
            )
        return attendance

    filters = []
    if child_id is not None:
        filters.append(Child.id == child_id)
    attendances = db.query(Attendances).filter(*filters).all()
    return attendances

