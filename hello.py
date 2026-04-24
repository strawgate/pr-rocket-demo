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


def greet_formally(name: str, title: str) -> str:
    """Return a formal greeting with a title."""
    return f"Hello, {title} {name}."


if __name__ == "__main__":
    print(greet("world"))
