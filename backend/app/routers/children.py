from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from db.session import get_db
from models.child import Child, ChildCreate, ChildUpdate
from models.base import ChildOutWithCommunity
from models.community import Community

router = APIRouter(prefix="/children")


@router.get("/{child_id}", summary="Get a child", response_model=ChildOutWithCommunity)
async def get_child(child_id: int, db: Session = Depends(get_db)):
    child = db.get(Child, child_id)
    if not child:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )
    return child


@router.get(
    "",
    summary="Get children",
    response_model=list[ChildOutWithCommunity],
    status_code=status.HTTP_200_OK,
)
async def get_children(
    community_id: Optional[str] = None,
    db: Session = Depends(get_db),
):
    filters = []
    if community_id is not None:
        filters.append(Child.community_id == community_id)
    return db.query(Child).filter(*filters).all()


@router.post(
    "",
    summary="Add a child",
    status_code=status.HTTP_201_CREATED,
    response_model=ChildOutWithCommunity,
)
async def add_child(child: ChildCreate, db: Session = Depends(get_db)):
    if (
        db.query(Child)
        .filter(
            Child.first_name == child.first_name,
            Child.last_name == child.last_name,
        )
        .first()
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="There already exists a child with the same first and last name.",
        )

    if not db.get(Community, child.community_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Community with ID {child.community_id} not found",
        )
    new_child = Child.from_orm(child)
    db.add(new_child)
    db.commit()
    db.refresh(new_child)
    return new_child


@router.patch(
    "/{child_id}",
    summary="Update a child",
    response_model=Child,
    status_code=status.HTTP_200_OK,
)
async def update_child(
    child_id: int, child: ChildUpdate, db: Session = Depends(get_db)
):
    db_child = db.get(Child, child_id)
    if not db_child:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Child with ID {child_id} not found",
        )
    child_data = child.model_dump(exclude_unset=True)
    db_child.sqlmodel_update(child_data)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child
