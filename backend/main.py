# main.py
# This is the main entry point for the FastAPI application.
# It sets up the application, including middleware and routes.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import lifespan
from core.config import settings
from routes.student_routes import router as student_router
# The FastAPI application is created with a lifespan function
#  that manages the database connection.
app = FastAPI(lifespan=lifespan)
# CORS middleware is added to allow cross-origin requests
#  from specified origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)
# A simple health check endpoint is defined to verify that
#  the application is running.
@app.get("/health")
async def health():
    return {"status": "ok"}
# The student routes are included in the application, allowing
#  the application to handle requests related to student operations.
app.include_router(student_router)

# The application can be run using the command:
# uvicorn main:app --reload
