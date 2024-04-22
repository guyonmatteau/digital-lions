from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from db.session import get_db
from sqlalchemy.orm import Session
from db import schemas
from models import Attendance
from typing import Optional


router = APIRouter(prefix="/attendance")


@router.post("", summary="Add attendance of child to a workshop")
async def add_attendances(attendance: Attendance, db: Session = Depends(get_db)):
    new_attendance = schemas.Attendance(**attendance.dict())
    db.add(new_attendance)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Attendance(s) added successfully"},
    )


@router.get("", summary="Get attendances of children to workshops")
async def get_attendances(id: Optional[int] = None, db: Session = Depends(get_db)):
    attendances = db.query(schemas.Attendance).all()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"attendance": [attendance.as_dict() for attendance in attendances]},
    )
