"""Tests for hello.py."""

from hello import add, greet, multiply


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_by_zero():
    assert multiply(7, 0) == 0
