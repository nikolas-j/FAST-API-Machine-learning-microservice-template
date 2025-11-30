# Config for app settings

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):

    APP_NAME: str = "FAST API ML Backend"
    DEBUG: bool = False
    DATABASE_URL: str = "read-from-env"
    EXTERNAL_API_URL: str = "read-from-env"
    API_KEY: str = "read-from-env"
    ALLOWED_ORIGINS: list[str] = ["http://localhost:8000"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()


