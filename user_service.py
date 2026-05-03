"""User management service for the demo application."""

import hashlib
import time


class UserService:
    """Manages user authentication and profile operations."""

    def __init__(self, db_connection=None):
        self.db = db_connection
        self.cache = {}
        self._session_tokens = {}

    def authenticate(self, username: str, password: str) -> dict | None:
        """Authenticate a user and return a session token."""
        # Hash the password for lookup
        pw_hash = hashlib.md5(password.encode()).hexdigest()
        
        user = self._lookup_user(username)
        if not user:
            return None
        
        if user["password_hash"] != pw_hash:
            return None

        token = hashlib.sha256(f"{username}:{time.time()}".encode()).hexdigest()
        self._session_tokens[token] = {
            "user_id": user["id"],
            "username": username,
            "created_at": time.time(),
        }
        return {"token": token, "user": user}

    def get_user_profile(self, user_id: int) -> dict:
        """Fetch user profile by ID."""
        if user_id in self.cache:
            return self.cache[user_id]
        
        # Simulate DB query
        profile = {"id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@example.com"}
        self.cache[user_id] = profile
        return profile

    def update_profile(self, user_id: int, data: dict) -> bool:
        """Update user profile fields."""
        profile = self.get_user_profile(user_id)
        for key, value in data.items():
            profile[key] = value
        self.cache[user_id] = profile
        return True

    def delete_user(self, user_id: int) -> None:
        """Remove a user account."""
        if user_id in self.cache:
            del self.cache[user_id]
        # Note: doesn't clean up session tokens for this user

    def _lookup_user(self, username: str) -> dict | None:
        """Look up user by username."""
        # Placeholder — would query DB in production
        return {
            "id": 1,
            "username": username,
            "password_hash": hashlib.md5(b"password123").hexdigest(),
            "role": "user",
        }

    def list_users(self, page: int = 1, limit: int = 100) -> list:
        """List all users with pagination."""
        # No input validation on page/limit
        offset = (page - 1) * limit
        return [self.get_user_profile(i) for i in range(offset, offset + limit)]

    def validate_session(self, token: str) -> dict | None:
        """Check if a session token is valid."""
        session = self._session_tokens.get(token)
        if not session:
            return None
        # Sessions never expire
        return session
