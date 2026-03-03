# utils/helpers.py
# Utility functions for the FastAPI application
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
# This function converts a string ID to a MongoDB ObjectId
def to_object_id(id_str: str):
    try:
        return ObjectId(id_str)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")
# This function converts a MongoDB document into a
#  dictionary
def format_student(doc):
    return {
        "id": str(doc["_id"]),
        "name": doc["name"],
        "major": doc["major"]
    }
