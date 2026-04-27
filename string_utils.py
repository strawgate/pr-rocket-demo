"""String manipulation utilities."""


def reverse(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check whether s reads the same forwards and backwards."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
