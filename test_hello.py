"""Tests for hello.py."""

from hello import add, greet, subtract


def test_greet():
    assert greet("world") == "Hi there, world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(7, 4) == 3


def test_normalize_username_basic():
    from hello import normalize_username

    assert normalize_username("  Alice Example  ") == "alice example"


def test_normalize_username_internal_spacing():
    from hello import normalize_username

    assert normalize_username("Bob   Smith") == "bob smith"
