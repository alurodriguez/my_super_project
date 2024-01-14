from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from decouple import config
from app.core.config import settings

# SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
# SQLALCHEMY_DATABASE_URI = (
#     f"postgresql://{config('DB_USER')}:"
#     f"{config('DB_PASSWORD')}@{config('DB_HOST')}:"
#     f"{config('DB_PORT')}/{config('DB_NAME')}"
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    # connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
