import exceptions
from dependencies import ChildServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.api.child import ChildGetByIdOut, ChildGetOut, ChildPatchIn, ChildPostIn
from models.api.generic import RecordCreated

router = APIRouter(prefix="/children")


@router.get("/{child_id}", summary="Get a child by id", response_model=ChildGetByIdOut)
async def get_child(child_id: int, child_service: ChildServiceDependency):
    try:
        return child_service.get(child_id)
    except exceptions.ChildNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.get(
    "",
    summary="Get children",
    response_model=list[ChildGetOut] | None,
    status_code=status.HTTP_200_OK,
)
async def get_children(
    child_service: ChildServiceDependency,
    community_id: int = None,
):
    """Get list of children, optionally filtered by community."""

    return child_service.get_all()


@router.post(
    "",
    summary="Add a child",
    status_code=status.HTTP_201_CREATED,
    response_model=RecordCreated,
)
async def add_child(child_service: ChildServiceDependency, child: ChildPostIn):
    try:
        return child_service.create(child)
    except exceptions.ChildAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="There already exists a child with this name in team {child.team_id}",
        )
    except exceptions.TeamNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Team with ID {child.team_id} not found",
        )


@router.patch(
    "/{child_id}",
    summary="Update a child",
    response_model=ChildGetByIdOut,
    status_code=status.HTTP_200_OK,
)
async def update_child(
    child_service: ChildServiceDependency,
    child_id: int,
    child: ChildPatchIn,
):
    try:
        return child_service.update(object_id=child_id, obj=child)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )


@router.delete(
    "/{child_id}",
    summary="Delete a child",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_child(
    child_id: int, child_service: ChildServiceDependency, cascade: bool = False
):
    """Delete a child by ID. If cascade is set to True, also delete all
    related attendances."""
    try:
        child_service.delete(object_id=child_id, cascade=cascade)
    except exceptions.ChildHasAttendanceException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete child with id {child_id} because it has related "
            + "attendance records and 'cascade' is set to false.",
        )
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with id {child_id} not found",
        )
