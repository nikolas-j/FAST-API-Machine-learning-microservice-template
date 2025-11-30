# Config for app settings

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):

    APP_NAME: str = "ML Fullstack Demo"
    DATABASE_URL: str = "postgresql://user:pass@localhost/db"
    EXTERNAL_API_URL: str = "https://api.example.com/data"
    API_KEY: str | None = None
    MODEL_PATH: str = "models/model.pkl"
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()


