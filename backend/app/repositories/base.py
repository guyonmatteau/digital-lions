from typing import Generic, TypeVar

from dependencies.database import DatabaseDependency
from exceptions import ItemNotFoundException
from sqlalchemy import delete
from sqlmodel import SQLModel

Model = TypeVar("Model", bound=SQLModel)
ModelCreate = TypeVar("ModelCreate", bound=SQLModel)
ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelOut = TypeVar("ModelOut", bound=SQLModel)


class BaseRepository(Generic[Model]):
    """Generic repository template metaclass for all repositories that
    interact with a table in the database. Supports all classic CRUD
    operations as well as custom queries."""

    _model: type[Model]

    def __init__(self, db: DatabaseDependency):
        self._db: DatabaseDependency = db

    def create(self, obj: ModelCreate) -> ModelOut:
        """Create an object in the table."""
        new_obj = self._model.from_orm(obj)
        self._db.add(new_obj)
        self._db.commit()
        self._db.refresh(new_obj)
        return new_obj

    def delete(self, object_id: int) -> None:
        """Delete an object from the table."""
        obj = self._db.get(self._model, object_id)
        if not obj:
            raise ItemNotFoundException()
        self._db.delete(obj)
        self._db.commit()

    def delete_bulk(self, attr: str, value: str) -> None:
        """Delete all objects by an attribute matching a value."""
        statement = delete(self._model).where(getattr(self._model, attr) == value)
        print(statement)
        self._db.exec(statement)
        self._db.commit()

    def read(self, object_id: int) -> ModelOut | None:
        """Read an object from the table."""
        obj = self._db.get(self._model, object_id)
        if not obj:
            raise ItemNotFoundException()
        return obj

    def read_all(self) -> list[ModelOut] | None:
        """Read all objects from the table."""
        objects = self._db.query(self._model).all()
        return objects

    def filter(self, attr: str, value: str) -> list[ModelOut] | None:
        """Filter objects by an attribute."""
        objects = self._db.query(self._model).filter(getattr(self._model, attr) == value).all()
        return objects

    def update(self, object_id: int, obj: ModelUpdate) -> ModelOut:
        """Update an object in the table."""
        db_object = self._db.get(self._model, object_id)
        if not db_object:
            raise ItemNotFoundException()

        obj_data = obj.model_dump(exclude_unset=True)
        db_object.sqlmodel_update(obj_data)
        self._db.add(db_object)
        self._db.commit()
        self._db.refresh(db_object)
        return db_object

    def query(self, query: str) -> list[ModelOut]:
        """Execute a custom query."""
        objects = self._db.exec(query)
        return objects
