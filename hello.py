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


def absolute(n: int) -> int:
    """Return the absolute value of n."""
    return n if n >= 0 else -n


if __name__ == "__main__":
    print(greet("world"))
