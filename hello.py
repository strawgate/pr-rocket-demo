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


def clamp(value: int, low: int, high: int) -> int:
    """Clamp value between low and high (inclusive)."""
    if value < low:
        return low
    if value > high:
        return high
    return value
