"""A simple module for e2e testing PR Rocket."""

import re


def slugify_title(text: str) -> str:
    """Convert a title string to a URL-friendly slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


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
