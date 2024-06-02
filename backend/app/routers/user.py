import logging

from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User, UserCreate, UserLogin, UserOut, UserUpdate
from sqlmodel import Session

from typing import Annotated

from exceptions import ItemAlreadyExistsException, ItemNotFoundException
from app.repositories.base import UserRepository

logger = logging.getLogger()

router = APIRouter(prefix="/users", tags=["users"])



@router.post(
    "/login",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Login user",
)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email_address == user.email_address).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user.email_address} not found",
        )
    hashed_password, _ = _hash_password(user.password, db_user.salt)
    logger.info(
        f"db_user.hashed_password: {db_user.hashed_password}, hashed_password: {hashed_password}"
    )
    if db_user.hashed_password == hashed_password:
        return db_user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized"
    )


@router.get(
    "",
    response_model=list[UserOut],
    status_code=status.HTTP_200_OK,
    summary="List all users",
)
async def get_users(user_repository: Annotated[UserRepository, Depends()]):
    return user_repository.get_users()


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
async def create_user(user: UserCreate, user_repository: Annotated[UserRepository, Depends()]):
    try:
        return user_repository.add_user(user)
    except ItemAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

   
@router.get(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Get a user by ID",
)
async def read_user(user_id: int, user_repository: Annotated[UserRepository, Depends()]):
    try:
        return user_repository.get_user(user_id=user_id)
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

@router.patch(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Update a user by ID",
)
async def update_user(user_id: int, user: UserUpdate, user_repository: Annotated[UserRepository, Depends()]):
    try:
        return user_repository.update_user(user_id=user_id, user=user)
    except ItemNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )


