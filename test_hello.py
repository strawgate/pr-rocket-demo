"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_anagram():
    from hello import is_anagram
    assert is_anagram("listen", "silent")
    assert is_anagram("Astronomer", "Moon starer")
    assert not is_anagram("hello", "world")
    assert is_anagram("", "")
