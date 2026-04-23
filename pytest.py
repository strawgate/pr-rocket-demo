"""
A minimal pytest shim used by the custom test runner in this repository.
Provides:
- fixture(): decorator that returns the function unchanged (fixtures handled by runner)
- raises(): context manager asserting a block raises a given exception

This is intentionally minimal and only supports features used by the tests in this repo.
"""
from contextlib import ContextDecorator


def fixture(*args, **kwargs):
    """Return a no-op decorator so test modules defining fixtures can import pytest.fixture.
    The actual fixture invocation is performed by the custom test runner (run_tests.py).
    """
    def _decorator(f):
        return f

    return _decorator


class _Raises(ContextDecorator):
    def __init__(self, expected_exc):
        self.expected_exc = expected_exc
        self.caught = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc is None:
            raise AssertionError(f"Did not raise {self.expected_exc}")
        if not issubclass(exc_type, self.expected_exc):
            # Re-raise unexpected exceptions
            return False
        # Expected exception was raised; suppress it
        self.caught = exc
        return True


def raises(expected_exc):
    return _Raises(expected_exc)
