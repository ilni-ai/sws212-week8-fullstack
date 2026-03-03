# core/database.py
# This module sets up the MongoDB connection using Motor,
#  an asynchronous MongoDB driver.
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .config import settings
# The lifespan function is used to manage the lifecycle
#  of the MongoDB connection.
@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]

    await db.command("ping")

    app.state.mongo_client = client
    app.state.db = db
    # The yield statement allows the application to run
    #  while the connection is open.
    yield
    # After the application is done, the connection
    #  is closed.
    client.close()
