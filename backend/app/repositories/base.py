from fastapi import Depends
from typing import Annotated

import bcrypt
from db.session import get_db
from exceptions import ItemAlreadyExistsException, ItemNotFoundException

from sqlmodel import Session

from models.user import User, UserCreate, UserLogin, UserOut, UserUpdate


class UserRepository:
    """Repository to interact with User table from Postgres DB."""
    # note currently does also some business logic, to be moved to service layer later

    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self._db = db

    def get_users(self) -> list[User]:
        return self._db.query(User).all()

    def get_user(self, user_id: int) -> User:
        user = self._db.get(User, user_id)
        if not user:
            raise ItemNotFoundException()
        return user

    def add_user(self, user: UserCreate) -> UserOut:
        if self._db.query(User).filter(User.email_address == user.email_address).first():
            raise ItemAlreadyExistsException()
    
        # this should be part of the service
        hashed_password, salt = _hash_password(user.password)
        extra_data = {"hashed_password": hashed_password, "salt": salt}
        db_user = User.model_validate(user, update=extra_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    
    def update_user(self, user_id: int, user: UserUpdate) -> UserOut:
        db_user = self._db.get(User, user_id)
        if not db_user:
            raise ItemNotFoundException()
        user_data = user.model_dump(exclude_unset=True)
        db_user.sql_update(user_data)
        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)
        return db_user

# hashing should actually be part of the service
def _hash_password(password: str, salt: bytes = None) -> [bytes, bytes]:
    """Hash password."""
    salt = salt or bcrypt.gensalt()
    logger.info(f"SALT: {salt}")
    hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return hashed_password, salt



