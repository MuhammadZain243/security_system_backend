from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Security System API"
    app_version: str = "0.1.0"
    app_env: str = "development"

    host: str = "127.0.0.1"
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def base_url(self) -> str:
        return f"http://{self.host}:{self.port}"


@lru_cache
def get_settings() -> Settings:
    return Settings()