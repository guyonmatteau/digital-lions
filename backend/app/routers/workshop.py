from typing import Optional

from dependencies.database import DatabaseDependency
from fastapi import APIRouter, HTTPException, status

# from models.attendance import AttendanceCreate
from models.child import Child
from models.community import Community
from models.out import WorkshopOut
from models.workshop import Workshop, WorkshopCreate
# from routers.attendance import add_attendance

router = APIRouter(prefix="/workshops")


@router.post(
    "",
    summary="Add workshop",
    status_code=status.HTTP_201_CREATED,
    response_model=WorkshopOut,
)
async def add_workshop(workshop: WorkshopCreate, db: DatabaseDependency):
    if (
        db.query(Workshop)
        .filter(
            Workshop.community_id == workshop.community_id,
            Workshop.date == workshop.date,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Workshop already exists for community ID {workshop.community_id} on date {workshop.date}",
        )
    if not db.query(Community).filter(Community.id == workshop.community_id).first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {workshop.community_id} not found",
        )
    if workshop.attendance is not None:
        for attendance in workshop.attendance:
            if not db.query(Child).filter(Child.id == attendance.child_id).first():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Child with ID {attendance.child_id} not found",
                )

    # create workshop
    new_workshop = Workshop.from_orm(workshop)
    db.add(new_workshop)
    db.commit()
    db.refresh(new_workshop)

    # add attendances for created workshop
    if workshop.attendance is not None:
        for attendance in workshop.attendance:
            new_attendance = AttendanceCreate(
                child_id=attendance.child_id,
                workshop_id=new_workshop.id,
                attendance=attendance.attendance,
            )
            await add_attendance(new_attendance, db)

    return new_workshop


@router.get("/{workshop_id}", summary="Get workshop by ID", response_model=WorkshopOut)
async def get_workshop(workshop_id: int, db: DatabaseDependency):
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
    response_model=Optional[list[WorkshopOut]],
)
async def get_workshops(
    db: DatabaseDependency,
    community_id: int | None = None,
    date: str | None = None,
):
    """Get the Workshop of a child to a workshop."""
    filters = []
    if community_id is not None:
        filters.nd(Workshop.community_id == community_id)
    if date is not None:
        filters.nd(Workshop.date == date)
    workshops = db.query(Workshop).filter(*filters).all()
    return workshops
