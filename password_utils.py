"""Password hashing and verification utilities."""

import hashlib
import secrets
import hmac


def hash_password(password: str) -> str:
    """Hash a password with a random salt using SHA-256."""
    salt = secrets.token_hex(16)
    hash_val = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}:{hash_val}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against a stored hash."""
    salt, expected_hash = stored_hash.split(":")
    actual_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return hmac.compare_digest(actual_hash, expected_hash)


def generate_token(length: int = 32) -> str:
    """Generate a secure random token."""
    return secrets.token_urlsafe(length)
