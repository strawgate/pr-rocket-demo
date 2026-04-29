"""Input validation utilities."""


def validate_email(email: str) -> bool:
    """Check if email has valid format."""
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    return len(local) > 0 and "." in domain


def validate_phone(phone: str) -> str:
    """Normalize and validate phone number."""
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) == 10:
        return f"+1{digits}"
    elif len(digits) == 11 and digits[0] == "1":
        return f"+{digits}"
    return ""


def validate_age(age) -> int | None:
    """Validate age is reasonable."""
    try:
        val = int(age)
        if 0 <= val <= 150:
            return val
    except (ValueError, TypeError):
        pass
    return None


def sanitize_html(text: str) -> str:
    """Remove HTML tags from text (basic)."""
    import re
    return re.sub(r"<[^>]+>", "", text)
