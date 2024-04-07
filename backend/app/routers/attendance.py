from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from db.session import SessionLocal
from sqlalchemy.orm import Session
from db import schemas
from models import Attendance

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/attendances", tags=["attendance"])



@router.post("")
async def add_attendances(
    attendances: list[Attendance], db: Session = Depends(get_db)
):
    new_attendances = [schemas.Attendance(**attendance.dict()) for attendance in attendances]
    db.bulk_save_objects(new_attendances)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content = {"message": "Attendance(s) added successfully"}
    )

@router.get("")
async def get_attendances(db: Session = Depends(get_db)):
    attendances = db.query(schemas.Attendance).all()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content = {"attendances": [attendance.as_dict() for attendance in attendances]}
    )



