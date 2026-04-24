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


def normalize_username(username: str) -> str:
    """Return a normalized username: stripped, lowercased, with collapsed whitespace."""
    return " ".join(username.split()).lower()


if __name__ == "__main__":
    print(greet("world"))
