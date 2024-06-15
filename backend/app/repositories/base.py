from typing import Union, Type, TypeVar, Generic

from dependencies.database import DatabaseDependency
from fastapi import Depends

from sqlmodel import SQLModel

from models.community import Community

from models.out import CommunityOut
from models.child import Child


Model = Community

T = TypeVar("T", bound=SQLModel)


class BaseRepository:
    """Generic repository template for all repositories that
    interact with a table in the database."""

    def __init__(self, model: Model, db: DatabaseDependency):
        self.db: DatabaseDependency = db
        self.model: Model = model

    def read_all(self) -> list[CommunityOut]:
        objects = self.db.query(self.model).all()
        print(f"OBJECTS: {objects}")
        return objects

    def read(self, object_id: int) -> list[Model]:
        object_ = self.db.get(self.model, object_id)
        if not object_:
            raise ItemNotFoundException()
        return object_

    def create(self, object_data: Model) -> Model:
        new_object = self.model.from_orm(object_data)
        self.db.add(new_object)
        self.db.commit()
        self.db.refresh(new_object)
        return new_object

    def update(self, object_id: int, object_data: Model) -> Model:
        db_object = self.db.get(self.model, object_id)
        if not db_object:
            raise ItemNotFoundException()

        object_data = self.model.model_dump(exclude_unset=True)
        db_object.sqlmodel_update(object_data)
        self.db.add(db_object)
        self.db.commit()
        self.db.refresh(db_object)
        return db_object
