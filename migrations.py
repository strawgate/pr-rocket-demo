"""Database migration runner (SQLite)."""

import sqlite3
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class Migration:
    version: int
    name: str
    sql: str


def get_current_version(conn: sqlite3.Connection) -> int:
    """Get the current schema version."""
    conn.execute("CREATE TABLE IF NOT EXISTS schema_version (version INTEGER PRIMARY KEY)")
    row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
    return row[0] or 0


def apply_migrations(db_path: str, migrations: list[Migration]) -> int:
    """Apply pending migrations. Returns number applied."""
    conn = sqlite3.connect(db_path)
    current = get_current_version(conn)
    applied = 0

    for migration in sorted(migrations, key=lambda m: m.version):
        if migration.version <= current:
            continue
        conn.executescript(migration.sql)
        conn.execute("INSERT INTO schema_version (version) VALUES (?)", (migration.version,))
        conn.commit()
        applied += 1
        print(f"  Applied migration {migration.version}: {migration.name}")

    conn.close()
    return applied
