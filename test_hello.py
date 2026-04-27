"""Tests for hello.py."""

from hello import add, clamp, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_clamp_within_range():
    assert clamp(5, 1, 10) == 5


def test_clamp_below_low():
    assert clamp(0, 1, 10) == 1


def test_clamp_above_high():
    assert clamp(11, 1, 10) == 10


def test_clamp_at_low():
    assert clamp(1, 1, 10) == 1


def test_clamp_at_high():
    assert clamp(10, 1, 10) == 10
