import logging

from exceptions import ItemAlreadyExistsException, ItemNotFoundException
from models.community import Community, CommunityCreate, CommunityUpdate
from models.community import Community
from models.out import CommunityOut
from repositories.base import BaseRepository

logger = logging.getLogger()


# class CommunityRepository(BaseRepository):
#     """Repository to interact with Community table.""""
#
#     def read_all(self) -> list[Community]:
#         return self.db.query(Community).all()
#
#     def read(self, community_id: int) -> Community:
#         community = self.db.get(Community, community_id)
#         if not community:
#             raise ItemNotFoundException()
#         return community
#
#     def create(self, community: CommunityCreate) -> CommunityOut:
#         new_community = Community.from_orm(community)
#         self.db.add(new_community)
#         self.db.commit()
#         self.db.refresh(new_community)
#         return new_community
#
#     def update(self, community_id: int, community: CommunityUpdate) -> CommunityOut:
#         db_community = self.db.get(Community, community_id)
#         if not db_community:
#             raise ItemNotFoundException("Community not found")
#         community_data = community.model_dump(exclude_unset=True)
#         db_community.sqlmodel_update(community_data)
#         self.db.add(db_community)
#         self.db.commit()
#         self.db.refresh(db_community)
#         return db_community
