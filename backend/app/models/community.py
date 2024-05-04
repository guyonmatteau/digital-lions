from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class CommunityBase(SQLModel):
    name: str = Field()


class CommunityCreate(CommunityBase):
    pass


class CommunityUpdate(CommunityCreate):
    """Schema for updating a community."""

    is_active: bool = True


class Community(CommunityUpdate, table=True):
    """Schema for community in database."""

    id: int = Field(default=None, primary_key=True)

    # workshops: list["Workshop"] | None = Relationship(back_populates="community")
    children: list["Child"] | None = Relationship(back_populates="community")

    created_at: datetime = datetime.now()
    # TODO add updated_at default factory
    # updated_at: datetime = datetime.now()


class CommunityOut(CommunityBase):
    id: int
