from sqlalchemy import Boolean, Column, Integer, String

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
    community = Column(String)
    child = Column(String)
    cycle = Column(Integer)
    attendance = Column(Boolean)

