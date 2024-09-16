import logging

from core import exceptions
from core.auth import APIKeyDependency, BearerTokenDependency
from core.dependencies import UserServiceDependency
from fastapi import APIRouter, HTTPException, status
from models.api.generic import Message, RecordCreated
from models.api.user import (
    UserGetByIdOut,
    UserPatchIn,
    UserPostIn,
    UserPostInviteIn,
    UserPostLoginIn,
)
from pydantic import EmailStr

logger = logging.getLogger()

router = APIRouter(prefix="/users", dependencies=[APIKeyDependency, BearerTokenDependency])


@router.post(
    "/login",
    response_model=UserGetByIdOut,
    status_code=status.HTTP_200_OK,
    summary="Login user",
)
async def login(user: UserPostLoginIn, user_service: UserServiceDependency):
    try:
        return user_service.login(user=user)
    except exceptions.UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    except exceptions.UserUnauthorizedException as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=list[UserGetByIdOut],
    status_code=status.HTTP_200_OK,
    summary="List all users",
)
async def get_users(user_service: UserServiceDependency):
    return user_service.read_all()


@router.post(
    "",
    response_model=RecordCreated,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
async def create_user(user: UserPostIn, user_service: UserServiceDependency):
    try:
        return user_service.create(user)
    except exceptions.UserEmailAlreadyExistsException as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc))


@router.get(
    "/{user_id}",
    response_model=UserGetByIdOut,
    status_code=status.HTTP_200_OK,
    summary="Get a user by ID",
)
async def read_user(user_id: int, user_service: UserServiceDependency):
    try:
        return user_service.get(user_id=user_id)
    except exceptions.UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.patch(
    "/{user_id}",
    response_model=UserGetByIdOut,
    summary="Update a user by ID",
)
async def update_user(
    user_id: int,
    user: UserPatchIn,
    user_service: UserServiceDependency,
):
    try:
        return user_service.update(user_id=user_id, user=user)
    except exceptions.UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post(
    "/reset-password",
    response_model=Message,
    summary="Email user a link to reset password",
)
async def reset_password(
    email_address: EmailStr,
    user_service: UserServiceDependency,
):
    try:
        user_service.forgot_password(email_address=email_address)
    except exceptions.UserNotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post("/invite-user", response_model=Message, summary="Invite new user to platform.")
async def invite_user(user: UserPostInviteIn, user_service: UserServiceDependency):
    try:
        user_service.invite_user(user=user)
    except:
        pass

