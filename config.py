"""Configuration management with environment variable support."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Application configuration loaded from environment."""
    debug: bool = False
    port: int = 8080
    host: str = "0.0.0.0"
    db_url: str = "sqlite:///app.db"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            debug=os.getenv("DEBUG", "").lower() in ("1", "true"),
            port=int(os.getenv("PORT", "8080")),
            host=os.getenv("HOST", "0.0.0.0"),
            db_url=os.getenv("DATABASE_URL", "sqlite:///app.db"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )
