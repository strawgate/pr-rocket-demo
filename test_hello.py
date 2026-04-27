"""Tests for hello.py."""

from hello import add, greet, squared, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_squared():
    assert squared(4) == 16


def test_squared_zero():
    assert squared(0) == 0


def test_squared_negative():
    assert squared(-3) == 9


def test_squared_one():
    assert squared(1) == 1
