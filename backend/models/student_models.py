# models/student_models.py
# This file defines the Pydantic models for the Student
#  entity, which are used for data validation and
#  serialization in the FastAPI application.
from pydantic import BaseModel, Field
# The StudentIn model is used for incoming data when
#  creating or updating a student.
class StudentIn(BaseModel):
    name: str = Field(..., min_length=1)
    major: str = Field(..., min_length=1)
# The StudentOut model is used for outgoing data when
#   returning student information in API responses.
class StudentOut(BaseModel):
    id: str
    name: str
    major: str
