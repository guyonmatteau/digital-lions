from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


# class AttendanceBase(SQLModel):
#     """Base class for attendance model."""
#
#     child_id: int = Field(foreign_key="children.id", exclude=True)
#     attendance: str
#
#     @field_validator("attendance")
#     def validate_attendance(cls, v):
#         if v not in ["present", "absent", "cancelled"]:
#             raise ValueError("Attendance must be either 'present' or 'absent' or 'cancelled'")
#         return v
#
#
# class AttendanceCreate(AttendanceBase):
#     """Data model for creating an attendance."""
#
#     workshop_id: int = Field(foreign_key="workshops.id")
#

# class Attendance(SQLModel, table=True):
#     """Data model for attendance of a child in a workshop."""
#
#     __tablename__ = "attendances"
#
#     id: int = Field(default=None, primary_key=True)
#
#     child: "Child" = Relationship(back_populates="attendances")
#     workshop: "Workshop" = Relationship(back_populates="attendances")
