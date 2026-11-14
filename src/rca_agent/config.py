from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration, read from RCA_* environment variables or a .env file."""

    model_config = SettingsConfigDict(
        env_prefix="RCA_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    loki_url: str = "http://localhost:3100"
    prometheus_url: str = "http://localhost:9090"
    kube_context: str | None = None
    kube_namespace: str = "default"
    chroma_path: Path = Path(".chroma")
    slack_webhook_url: SecretStr | None = None
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide settings instance."""
    return Settings()
