import exceptions
from dependencies.services import AttendanceServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.out import AttendanceOutWithChild

router = APIRouter(prefix="/attendance")


@router.get(
    "/{attendance_id}",
    response_model=AttendanceOutWithChild,
    summary="Get attendance of child to a workshop.",
)
async def get_attendance(attendance_id: int, attendance_service: AttendanceServiceDependency):
    try:
        return attendance_service.get_attendance(attendance_id)
    except exceptions.AttendanceNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attendance not found")


@router.get(
    "",
    summary="Get attendances of children to workshops",
    status_code=status.HTTP_200_OK,
    response_model=list[AttendanceOutWithChild] | None,
)
async def get_attendances(
    attendance_service: AttendanceServiceDependency,
    child_id: int | None = None,
    community_id: int | None = None,
):
    """Get all the attendances."""
    return attendance_service.get_attendances()
