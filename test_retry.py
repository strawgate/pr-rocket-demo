"""Tests for retry utility."""

from retry import retry


def test_retry_success_first_try():
    calls = []
    def fn():
        calls.append(1)
        return "ok"
    assert retry(fn) == "ok"
    assert len(calls) == 1


def test_retry_eventual_success():
    calls = []
    def fn():
        calls.append(1)
        if len(calls) < 3:
            raise ValueError("not yet")
        return "done"
    assert retry(fn, max_attempts=3, base_delay=0.01) == "done"
    assert len(calls) == 3
