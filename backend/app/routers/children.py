from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from models.child import Child, ChildCreate, ChildUpdate
from models.out import ChildOutWithCommunity
from repositories.children import ChildrenRepository

router = APIRouter(prefix="/children")


@router.get("/{child_id}", summary="Get a child", response_model=ChildOutWithCommunity)
async def get_child(
    child_id: int, children_repository: Annotated[ChildrenRepository, Depends()]
):
    try:
        return children_repository.get_child(child_id=child_id)
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )


@router.get(
    "",
    summary="Get children",
    response_model=list[ChildOutWithCommunity],
    status_code=status.HTTP_200_OK,
)
async def get_children(
    children_repository: Annotated[ChildrenRepository, Depends()],
    community_id: str | None = None,
):
    return children_repository.get_children(community_id=community_id)


@router.post(
    "",
    summary="Add a child",
    status_code=status.HTTP_201_CREATED,
    response_model=ChildOutWithCommunity,
)
async def add_child(
    child: ChildCreate, children_repository: Annotated[ChildrenRepository, Depends()]
):
    try:
        return children_repository.add_child(child=child)
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
    children_repository: Annotated[ChildrenRepository, Depends()],
):
    try:
        return children_repository.update_child(child_id=child_id, child=child)
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )
