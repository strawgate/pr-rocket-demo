"""A simple module for e2e testing PR Rocket."""

import re


def slugify_title(text: str) -> str:
    """Convert a title string to a URL-friendly slug.

    Lowercases the text, then collapses underscores and any sequence of
    repeated punctuation/whitespace into a single hyphen.
    """
    text = text.lower()
    text = re.sub(r"[_\s]+", "-", text)       # collapse underscores and whitespace
    text = re.sub(r"[^a-z0-9-]+", "-", text)  # replace remaining non-alphanumeric with hyphen
    text = re.sub(r"-+", "-", text)            # collapse repeated hyphens
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
