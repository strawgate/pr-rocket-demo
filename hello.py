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


def count_vowels(s: str) -> int:
    """Return the number of vowels in s (case-insensitive, English vowels only)."""
    return sum(1 for c in s.lower() if c in "aeiou")
