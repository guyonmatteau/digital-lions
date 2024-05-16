import logging

import bcrypt
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import User, UserCreate, UserLogin, UserOut, UserUpdate
from sqlmodel import Session

logger = logging.getLogger()

router = APIRouter(prefix="/users", tags=["users"])


def _hash_password(password: str, salt: bytes = None) -> [bytes, bytes]:
    """Hash password."""
    salt = salt or bcrypt.gensalt()
    logger.info(f"SALT: {salt}")
    hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return hashed_password, salt


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
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email_address == user.email_address).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    hashed_password, salt = _hash_password(user.password)
    extra_data = {"hashed_password": hashed_password, "salt": salt}
    db_user = User.model_validate(user, update=extra_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Get a user by ID",
)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.patch(
    "/{user_id}",
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    summary="Update a user by ID",
)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    user_data = user.model_dump(exclude_unset=True)
    db_user.sql_update(user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
