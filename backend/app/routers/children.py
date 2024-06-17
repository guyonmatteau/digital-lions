from dependencies.repositories import ChildRepositoryDependency
from exceptions import ItemAlreadyExistsException, ItemNotFoundException
from fastapi import APIRouter, HTTPException, status
from models.child import Child, ChildCreate, ChildUpdate
from models.out import ChildOut, ChildOutWithCommunity

router = APIRouter(prefix="/children")


@router.get("/{child_id}", summary="Get a child", response_model=ChildOutWithCommunity)
async def get_child(child_id: int, child_repository: ChildRepositoryDependency):
    try:
        return child_repository.read(child_id)
    except ItemNotFoundException:
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
    child_repository: ChildRepositoryDependency,
    community_id: str | None = None,
):
    return child_repository.read_all()


@router.post(
    "",
    summary="Add a child",
    status_code=status.HTTP_201_CREATED,
    response_model=ChildOut,
)
async def add_child(child: ChildCreate, child_repository: ChildRepositoryDependency):
    try:
        return child_repository.create(child)
    except ItemAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="There already exists a child with the same first and last name.",
        )
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Community with ID {child.community_id} not found",
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
    child_repository: ChildRepositoryDependency,
):
    try:
        return child_repository.update(object_id=child_id, obj=child)
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )
