"""Input validation helpers."""

import re


def validate_email(email: str) -> bool:
    """Check if email has valid format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_url(url: str) -> bool:
    """Check if URL has valid http/https format."""
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))


def sanitize_input(text: str) -> str:
    """Remove potentially dangerous characters from user input."""
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove null bytes
    text = text.replace("\x00", "")
    return text.strip()
