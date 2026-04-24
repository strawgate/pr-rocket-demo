"""Tests for hello.py."""

from hello import add, greet, greet_formally, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_greet_formally():
    assert greet_formally("Ada", "Dr.") == "Hello, Dr. Ada."
