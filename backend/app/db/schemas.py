from sqlalchemy import Boolean, Column, Integer, String

from db.session import Base


class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    day = Column(String)
    community = Column(String)
    child = Column(String)
    cycle = Column(Integer)
    attendance = Column(Boolean)

