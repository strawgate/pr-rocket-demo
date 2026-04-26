"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_count_vowels():
    from hello import count_vowels
    assert count_vowels("hello") == 2
    assert count_vowels("Programming") == 3
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0
