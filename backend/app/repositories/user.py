import logging

import bcrypt
from exceptions import ItemAlreadyExistsException, ItemNotFoundException, UserUnauthorizedException
from models.api.user import UserCreate, UserUpdate
from models.db.user import User
from models.out import UserOut
from repositories.base import BaseRepository

logger = logging.getLogger()


# hashing should actually be part of the service
def _hash_password(password: str, salt: bytes = None) -> [bytes, bytes]:
    """Hash password."""
    salt = salt or bcrypt.gensalt()
    logger.info(f"SALT: {salt}")
    hashed_password = bcrypt.hashpw(bytes(password, "utf-8"), salt)
    return hashed_password, salt


class UserRepository(BaseRepository):
    """Repository to interact with User table from Postgres db."""

    # note this class currently does also some business logic, to be moved to service layer later
    def get_users(self) -> list[User]:
        return self.db.query(User).all()

    def get_user(self, user_id: int) -> User:
        user = self.db.get(User, user_id)
        if not user:
            raise ItemNotFoundException()
        return user

    def add_user(self, user: UserCreate) -> UserOut:
        if self.db.query(User).filter(User.email_address == user.email_address).first():
            raise ItemAlreadyExistsException()

        # this should be part of the service
        hashed_password, salt = _hash_password(user.password)
        extra_data = {"hashed_password": hashed_password, "salt": salt}
        db_user = User.model_validate(user, update=extra_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdate) -> UserOut:
        db_user = self.db.get(User, user_id)
        if not db_user:
            raise ItemNotFoundException()
        user_data = user.model_dump(exclude_unset=True)
        db_user.sqlmodel_update(user_data)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def login_user(self, user: User) -> UserOut:
        db_user = self.db.query(User).filter(User.email_address == user.email_address).first()
        if not db_user:
            raise ItemNotFoundException()
        hashed_password, _ = _hash_password(user.password, db_user.salt)
        if db_user.hashed_password != hashed_password:
            raise UserUnauthorizedException()
        return db_user
