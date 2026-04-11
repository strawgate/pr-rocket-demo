"""Tests for hello.py."""

from hello import greet, add


def test_greet():
    assert greet("world") == "Hello, world!"


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    from hello import multiply
    assert multiply(3, 4) == 11  # deliberately wrong
