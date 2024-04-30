from typing import Optional

from db.models import Child, Community
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session

router = APIRouter(prefix="/children")


@router.get(
    "",
    summary="Get children",
    response_model=list[Child],
    status_code=status.HTTP_200_OK,
)
async def get_children(
    child_id: Optional[int] = None,
    community: Optional[str] = None,
    db: Session = Depends(get_db),
):
    filters = []
    if child_id is not None:
        filters.append(Child.id == child_id)
    if community is not None:
        filters.append(Child.community == community)
    children = db.query(Child).filter(*filters).all()
    return children


@router.post(
    "", summary="Add a child", status_code=status.HTTP_201_CREATED, response_model=Child
)
async def add_child(child: Child, db: Session = Depends(get_db)):
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

    db.add(child)
    db.commit()
    db.refresh(child)
    return child


@router.put(
    "/{child_id}",
    summary="Update a child",
    response_model=Child,
    status_code=status.HTTP_200_OK,
)
async def update_child(child_id: int, child: Child, db: Session = Depends(get_db)):
    db_child = db.get(Child, child_id)
    if not db_child:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": f"Child with ID {child_id} not found"},
        )
    child_data = child.model_dump(exclude_unset=True)
    db_child.sqlmodel_update(child_data)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child
