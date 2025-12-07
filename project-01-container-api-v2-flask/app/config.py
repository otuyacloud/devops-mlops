# app/config.py
import os


class Config:
    APP_NAME = "Project 01 Container API (Flask)"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://app_user:app_password@db:5432/app_db",
    )
