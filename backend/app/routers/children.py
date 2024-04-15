from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from db.session import get_db
from sqlalchemy.orm import Session
from db import schemas
from models import Child 
from typing import List, Optional


router = APIRouter(prefix="/children")

@router.get("", summary="Get children")
async def get_children(child_id: Optional[int] = None, community: Optional[str] = None, db: Session = Depends(get_db)):
    filters = []
    if child_id is not None:
        filters.append(schemas.Child.id == child_id)
    if community is not None:
        filters.append(schemas.Child.community == community)  
    children = db.query(schemas.Child).filter(*filters).all()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"children": [child.as_dict() for child in children]},
    )

@router.post("", summary="Add a child")
async def add_child(child: Child, db: Session = Depends(get_db)):
    if db.query(schemas.Child).filter(schemas.Child.first_name == child.first_name, schemas.Child.last_name == child.last_name).first():
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "There already exists a child with the same first and last name."},
        ) 

    new_child = schemas.Child(**child.dict())
    db.add(new_child)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=new_child.as_dict(),
    )

@router.put("/{child_id}", summary="Update a child")
async def update_child(child_id: int, child: Child, db: Session = Depends(get_db)):
    db_child = db.query(schemas.Child).filter(schemas.Child.id == child_id).first()
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



