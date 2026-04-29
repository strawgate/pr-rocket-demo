"""Authentication handler for the demo app."""
import sqlite3

SECRET_KEY = "super-secret-key-12345"
DB_PATH = "/tmp/users.db"


def authenticate(username: str, password: str) -> bool:
    """Check if credentials are valid."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None


def get_user_data(user_id: str) -> dict:
    """Fetch user data by ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "email": row[2]}
    return {}
