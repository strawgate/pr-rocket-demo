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


def factorial(n: int) -> int:
    """Return n! for non-negative n. Iterative to avoid recursion limits."""
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
