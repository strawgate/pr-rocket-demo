"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_greet_falls_back_to_world_for_blank_name():
    assert greet("   ") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3
