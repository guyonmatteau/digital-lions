import logging

from exceptions import ItemAlreadyExistsException, ItemNotFoundException
from models.child import Child, ChildCreate, ChildUpdate
from models.community import Community
from models.out import ChildOut
from repositories.base import BaseRepository

logger = logging.getLogger()


class ChildrenRepository(BaseRepository):
    """Repository to interact with Children table from Postgres Database"""

    def get_children(self, community_id: str = None) -> list[Child]:
        filters = []
        if community_id is not None:
            filters.append(Child.community_id == community_id)
        return self.db.query(Child).filter(*filters).all()

    def get_child(self, child_id: int) -> Child:
        child = self.db.get(Child, child_id)
        if not child:
            raise ItemNotFoundException()
        return child

    def add_child(self, child: ChildCreate) -> ChildOut:
        if (
            self.db.query(Child)
            .filter(
                Child.first_name == child.first_name, Child.last_name == child.last_name
            )
            .first()
        ):
            raise ItemAlreadyExistsException()

        if not self.db.get(Community, child.community_id):
            raise ItemNotFoundException()

        new_child = Child.from_orm(child)
        self.db.add(new_child)
        self.db.commit()
        self.db.refresh(new_child)
        return new_child

    def update_child(self, child_id: int, child: ChildUpdate) -> ChildOut:
        db_child = self.db.get(Child, child_id)
        if not db_child:
            raise ItemNotFoundException()

        child_data = child.model_dump(exclude_unset=True)
        db_child.sqlmodel_update(child_data)
        self.db.add(db_child)
        self.db.commit()
        self.db.refresh(db_child)
        return db_child
