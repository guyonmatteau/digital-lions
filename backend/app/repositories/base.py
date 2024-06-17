from typing import Generic, TypeVar

from dependencies.database import DatabaseDependency
from exceptions import ItemNotFoundException
from models import child, community
from models.out import ChildOut, CommunityOut

Model = TypeVar("Model", community.Community, child.Child)
ModelCreate = TypeVar("ModelCreate", community.CommunityCreate, child.ChildCreate)
ModelUpdate = TypeVar("ModelUpdate", community.CommunityUpdate, child.ChildUpdate)
ModelOut = TypeVar("ModelOut", CommunityOut, ChildOut)


class BaseRepository(Generic[Model]):
    """Generic repository template metaclass for all repositories that
    interact with a table in the database. Supports all classic CRUD
    operations as well as custom queries."""

    model: type[Model]

    def __init__(self, db: DatabaseDependency):
        self.db: DatabaseDependency = db

    def create(self, obj: ModelCreate) -> ModelOut:
        """Create an object in the table."""
        new_obj = self.model.from_orm(obj)
        self.db.add(new_obj)
        self.db.commit()
        self.db.refresh(new_obj)
        return new_obj

    def read(self, object_id: int) -> ModelOut:
        """Read an object from the table."""
        obj = self.db.get(self.model, object_id)
        if not obj:
            raise ItemNotFoundException()
        return obj

    def read_all(self) -> list[ModelOut]:
        """Read all objects from the table."""
        objects = self.db.query(self.model).all()
        return objects

    def update(self, object_id: int, obj: ModelUpdate) -> ModelOut:
        """Update an object in the table."""

        db_object = self.db.get(self.model, object_id)
        if not db_object:
            raise ItemNotFoundException()

        obj_data = obj.model_dump(exclude_unset=True)
        db_object.sqlmodel_update(obj_data)
        self.db.add(db_object)
        self.db.commit()
        self.db.refresh(db_object)
        return db_object

    def query(self, query: str) -> list[ModelOut]:
        """Execute a custom query."""
        objects = self.db.execute(query)
        return objects
