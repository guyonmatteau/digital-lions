from pydantic import BaseModel


class Attendance(BaseModel):
    day: str
    community: str
    child: str
    cycle: int
    attendance: bool
