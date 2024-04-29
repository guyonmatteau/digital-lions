from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from db.session import get_db
from sqlmodel import Session
from db.models import Child 
from typing import Optional


router = APIRouter(prefix="/children")


@router.get("", summary="Get children")
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

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"children": [child.as_dict() for child in children]},
    )


@router.post("", summary="Add a child")
async def add_child(child: Child, db: Session = Depends(get_db)):
    if (
        db.query(Child)
        .filter(
            Child.first_name == child.first_name,
            Child.last_name == child.last_name,
        )
        .first()
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "There already exists a child with the same first and last name."
            },
        )

    new_child = Child(**child.dict())
    db.add(new_child)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=new_child.as_dict(),
    )


@router.put("/{child_id}", summary="Update a child")
async def update_child(child_id: int, child: Child, db: Session = Depends(get_db)):
    db_child = db.query(Child).filter(Child.id == child_id).first()
    if db_child is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Child not found"},
        )

    for key, value in child.dict().items():
        setattr(db_child, key, value)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=db_child.as_dict(),
    )
