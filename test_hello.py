"""Tests for hello.py."""

from hello import greet, add


def test_greet():
    assert greet("world") == "Hello, world!"

