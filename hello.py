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


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def power(base: int, exp: int) -> int:
    """Raise base to exp power."""
    result = 1
    for _ in range(exp):
        result *= base
    return result


if __name__ == "__main__":
    print(greet("world"))
