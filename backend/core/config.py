# core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
# This file defines the configuration settings for the
#  application using Pydantic's BaseSettings.
class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str = "college_db"
    CORS_ORIGINS: List[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env")
# Create an instance of the Settings class to be used
#  throughout the application.
settings = Settings()
