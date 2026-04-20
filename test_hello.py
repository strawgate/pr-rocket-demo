"""Tests for hello.py."""

from hello import greet, add


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5
