import os
import secrets

from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    PROJECT_NAME: str = "Items API"
    PROJECT_VERSION: str = "1.0.0"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    # POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    # POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    # POSTGRES_PORT: str = os.getenv(
    #     "POSTGRES_PORT", "5432"
    # )  # default postgres port is 5432
    # POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    # SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # # SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    FIRST_SUPERUSER: EmailStr = os.getenv("FIRST_SUPERUSER") or "johndoe@example.com"
    FIRST_SUPERUSER_PASSWORD: str = os.getenv("FIRST_SUPERUSER_PASSWORD") or "secret"
    # DATABASE_URL = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:postgres@db:5432/postgres"

    class Config:
        env_file = ".env"


settings = Settings()