"""A simple module for e2e testing PR Rocket."""


def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hi there, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


if __name__ == "__main__":
    print(greet("world"))


def is_isogram(s: str) -> bool:
    """Return True if no letter occurs more than once (case-insensitive, ignores non-letters)."""
    letters = [c.lower() for c in s if c.isalpha()]
    return len(letters) == len(set(letters))
