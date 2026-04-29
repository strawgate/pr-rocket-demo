"""Configuration manager."""
import fcntl
import json
import os


class ConfigManager:
    """Manages application configuration."""

    def __init__(self):
        self.config = {}
        self._load()

    def _load(self):
        """Load config from file."""
        path = os.environ.get("CONFIG_PATH", "/etc/app/config.json")
        try:
            with open(path) as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}
        except json.JSONDecodeError:
            self.config = {}

    def get(self, key: str, default=None):
        """Get a config value."""
        return self.config.get(key, default)

    def set(self, key: str, value) -> None:
        """Set a config value and persist with file locking."""
        if not isinstance(key, str) or not key:
            raise ValueError("key must be a non-empty string")
        self.config[key] = value
        path = os.environ.get("CONFIG_PATH", "/etc/app/config.json")
        with open(path, "w") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                json.dump(self.config, f)
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)

    def get_database_url(self) -> str:
        """Get database URL from config or environment."""
        return self.config.get(
            "database_url",
            os.environ.get("DATABASE_URL", "")
        )

    def get_api_keys(self) -> dict:
        """Return all API keys from config."""
        return {k: v for k, v in self.config.items() if k.endswith("_api_key")}

    def reload(self) -> None:
        """Reload from disk."""
        self._load()

    def __repr__(self) -> str:
        return f"ConfigManager(keys={len(self.config)})"
