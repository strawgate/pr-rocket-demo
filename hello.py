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


def power(base: int, exp: int) -> int:
    """Return base raised to the power exp."""
    if exp < 0:
        raise ValueError("Negative exponents not supported for integer math")
    result = 1
    for _ in range(exp):
        result *= base
    return result
