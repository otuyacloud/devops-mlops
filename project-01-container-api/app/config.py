# app/config.py
from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "Project 01 Container API"
    environment: str = os.getenv("ENVIRONMENT", "local")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://app_user:app_password@db:5432/app_db",
    )


settings = Settings()
