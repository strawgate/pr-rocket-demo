"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_repeat():
    from hello import repeat
    assert repeat("ab", 3) == "ababab"
    assert repeat("x", 1) == "x"
    assert repeat("", 5) == ""
