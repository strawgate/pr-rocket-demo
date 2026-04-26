"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_reverse_words():
    from hello import reverse_words
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("") == ""
    assert reverse_words("one") == "one"
