from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.session import Base


class Serializer:
    def as_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))
        return d


class Attendance(Base, Serializer):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    day = Column(String)
    community = Column(String, nullable=False)
    child = Column(String, nullable=False)
    cycle = Column(Integer, nullable=True)
    attendance = Column(String)


class Child(Base, Serializer):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Integer, nullable=True)
    community = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Community(Base, Serializer):
    __tablename__ = "communities"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    active = Column(Boolean, default=True)
