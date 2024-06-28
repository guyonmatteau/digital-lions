
from dependencies.database import DatabaseDependency
from fastapi import APIRouter, HTTPException, status
from models.attendance import Attendance, AttendanceCreate
from models.child import Child
from models.out import AttendanceOutWithChild
from models.workshop import Workshop

router = APIRouter(prefix="/attendance")


@router.post(
    "",
    summary="Add attendance of child to a workshop",
    status_code=status.HTTP_201_CREATED,
    response_model=Attendance,
)
async def add_attendance(attendance: AttendanceCreate, db: DatabaseDependency):
    # validate that the workshop exist
    workshop = db.get(Workshop, attendance.workshop_id)
    if workshop is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workshop with ID {attendance.workshop_id} not found",
        )
    if (
        db.query(Attendance)
        .filter(
            Attendance.workshop_id == attendance.workshop_id,
            Attendance.child_id == attendance.child_id,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Attendance for workshop ID {attendance.workshop_id} already exists for child ID {attendance.child_id}",
        )

    new_attendance = Attendance.from_orm(attendance)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance


@router.get(
    "/{attendance_id}",
    response_model=list[AttendanceOutWithChild],
    summary="Get attendance of child to a workshop.",
)
async def get_attendance(attendance_id: int, db: DatabaseDependency):
    attendance = db.get(Attendance, attendance_id)
    if attendance is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found")
    return attendance


@router.get(
    "",
    summary="Get attendances of children to workshops",
    status_code=status.HTTP_200_OK,
    response_model=list[AttendanceOutWithChild] | None,
)
async def get_attendances(
    db: DatabaseDependency,
    child_id: int | None = None,
    community_id: int | None = None,
):
    """Get the attendance of a child to a workshop."""
    filters = []
    if child_id is not None:
        filters.append(Child.id == child_id)
    if community_id is not None:
        filters.append(Community.id == community_id)
    return db.query(Attendance).filter(*filters).all()
