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


def negate(n: int) -> int:
    """Return the negation of n."""
    return -n


if __name__ == "__main__":
    print(greet("world"))


def repeat(s: str, n: int) -> str:
    """Repeat string s exactly n times."""
    return s * n
