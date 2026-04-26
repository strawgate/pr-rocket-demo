"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_power():
    from hello import power
    assert power(2, 10) == 1024
    assert power(5, 0) == 1
    assert power(3, 4) == 81


def test_power_negative_exp_raises():
    import pytest
    from hello import power
    with pytest.raises(ValueError):
        power(2, -1)
