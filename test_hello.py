"""Tests for hello.py."""

from hello import add, greet, multiply, power, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9
