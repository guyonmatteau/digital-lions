from typing import Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

from db.session import get_db
from models.attendance import Attendance

router = APIRouter(prefix="/attendance")


@router.post(
    "",
    summary="Add attendance of child to a workshop",
    status_code=status.HTTP_201_CREATED,
    response_model=Attendance,
)
async def add_attendances(attendance: Attendance, db: Session = Depends(get_db)):
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

@router.get("/{attendance_id}", response_model=Attendance, summary="Get attendance of child to a workshop.")
async def get_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.get(Attendance, attendance_id)
    if attendance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found")
    return attendance

@router.get(
    "",
    summary="Get attendances of children to workshops",
    status_code=status.HTTP_200_OK,
    response_model=Optional[list[Attendance]],
)
async def get_attendances(
    child_id: Optional[int] = None,
    community_id: Optional[int] = None, 
    db: Session = Depends(get_db),
):
    """Get the attendance of a child to a workshop."""
    filters = []
    if child_id is not None:
        filters.append(Child.id == child_id)
    if community_id is not None:
        filters.append(Community.id == community_id)
    return db.query(Attendance).filter(*filters).all()
