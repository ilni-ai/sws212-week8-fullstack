# routes/student_routes.py
# This file defines the API routes for managing students in
#  the application.
from fastapi import APIRouter, HTTPException, Request, status
from typing import List
from models.student_models import StudentIn, StudentOut
from utils.helpers import to_object_id, format_student
# The APIRouter allows us to group related routes together. 
# We set a prefix of "/students"
router = APIRouter(prefix="/students", tags=["students"])
# Each route corresponds to a CRUD operation for the Student
#  resource.
@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentIn, request: Request):
    db = request.app.state.db
    result = await db.students.insert_one(student.model_dump())
    created = await db.students.find_one({"_id": result.inserted_id})
    return format_student(created)

@router.get("/", response_model=List[StudentOut])
async def list_students(request: Request):
    db = request.app.state.db
    docs = await db.students.find().to_list(100)
    return [format_student(d) for d in docs]

@router.put("/{student_id}", response_model=StudentOut)
async def update_student(student_id: str, student: StudentIn, request: Request):
    db = request.app.state.db
    oid = to_object_id(student_id)

    await db.students.update_one(
        {"_id": oid},
        {"$set": student.model_dump()}
    )

    updated = await db.students.find_one({"_id": oid})
    return format_student(updated)

@router.delete("/{student_id}")
async def delete_student(student_id: str, request: Request):
    db = request.app.state.db
    oid = to_object_id(student_id)

    await db.students.delete_one({"_id": oid})
    return {"message": "Deleted"}
