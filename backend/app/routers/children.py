import exceptions
from dependencies.services import ChildServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.child import Child, ChildCreate, ChildUpdate
from models.out import ChildOut, ChildOutDeep, RecordCreated

router = APIRouter(prefix="/children")


@router.get("/{child_id}", summary="Get a child by ID", response_model=ChildOutDeep)
async def get_child(child_id: int, child_service: ChildServiceDependency):
    try:
        return child_service.get(child_id)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )


@router.get(
    "",
    summary="Get children",
    response_model=list[ChildOut],
    status_code=status.HTTP_200_OK,
)
async def get_children(
    child_service: ChildServiceDependency,
):
    return child_service.get_all()


@router.post(
    "",
    summary="Add a child",
    status_code=status.HTTP_201_CREATED,
    response_model=RecordCreated,
)
async def add_child(child: ChildCreate, child_service: ChildServiceDependency):
    try:
        return child_service.create(child)
    except exceptions.ItemAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="There already exists a child with the same first and last name.",
        )
    except exceptions.TeamNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Team with ID {child.team_id} not found",
        )


@router.patch(
    "/{child_id}",
    summary="Update a child",
    response_model=Child,
    status_code=status.HTTP_200_OK,
)
async def update_child(
    child_id: int,
    child: ChildUpdate,
    child_service: ChildServiceDependency,
):
    try:
        return child_service.update(object_id=child_id, obj=child)
    except exceptions.ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )
