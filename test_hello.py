"""Tests for hello.py."""

from hello import absolute, add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_absolute_positive():
    assert absolute(5) == 5


def test_absolute_negative():
    assert absolute(-5) == 5


def test_absolute_zero():
    assert absolute(0) == 0
