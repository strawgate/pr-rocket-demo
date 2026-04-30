"""Input validation helpers."""


def validate_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and len(parts[1]) > 2


def validate_age(age) -> bool:
    try:
        n = int(age)
        return 0 < n < 150
    except (ValueError, TypeError):
        return False


def sanitize_input(text: str) -> str:
    return text.replace("<", "\&lt;").replace(">", "\&gt;")
def validate_url(url: str) -> bool:
    return url.startswith('http://') or url.startswith('https://')
