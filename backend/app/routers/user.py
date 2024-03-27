from fastapi import APIRouter, Request, status, Depends
from fastapi.responses import JSONResponse
from db.session import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db.models import User

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/users", tags=["users"])

# class User(BaseModel):
    # # id: int
    # name: str
    # email: str
    # password: str
    # role: str


@router.get("/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user: 
        return user
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})


# @router.post("")
# async def create_user(user: User, db: Session = Depends(get_db)):
    # user_id = 2
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content={"id": user_id})

# @router.put("/{user_id}")
