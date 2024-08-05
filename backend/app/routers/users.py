import logging
from typing import Annotated

from database.repositories import UserRepository
from exceptions import ItemAlreadyExistsException, ItemNotFoundException, UserUnauthorizedException
from fastapi import APIRouter, Depends, HTTPException, status
from models.api.generic import RecordCreated
from models.api.user import UserCreate, UserGetByIdOut, UserLogin, UserUpdate

logger = logging.getLogger()

router = APIRouter(prefix="/users")


@router.post(
    "/login",
    response_model=UserGetByIdOut,
    status_code=status.HTTP_200_OK,
    summary="Login user",
)
async def login(user: UserLogin, user_repository: Annotated[UserRepository, Depends()]):
    try:
        return user_repository.login_user(user=user)
    except ItemNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user.email_address} not found",
        )
    except UserUnauthorizedException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized")


@router.get(
    "",
    response_model=list[UserGetByIdOut],
    status_code=status.HTTP_200_OK,
    summary="List all users",
)
async def get_users(user_repository: Annotated[UserRepository, Depends()]):
    return user_repository.get_users()


@router.post(
    "",
    response_model=RecordCreated,
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
    response_model=UserGetByIdOut,
    status_code=status.HTTP_200_OK,
    summary="Get a user by ID",
)
async def read_user(user_id: int, user_repository: Annotated[UserRepository, Depends()]):
    try:
        return user_repository.get_user(user_id=user_id)
    except ItemNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.patch(
    "/{user_id}",
    response_model=UserGetByIdOut,
    summary="Update a user by ID",
)
async def update_user(
    user_id: int,
    user: UserUpdate,
    user_repository: Annotated[UserRepository, Depends()],
):
    try:
        return user_repository.update_user(user_id=user_id, user=user)
    except ItemNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except ItemNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
