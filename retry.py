"""Retry utility with exponential backoff."""

import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(fn: Callable[[], T], max_attempts: int = 3, base_delay: float = 0.5) -> T:
    """Retry fn with exponential backoff."""
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception:
            if attempt == max_attempts - 1:
                raise
            time.sleep(base_delay * (2 ** attempt))
    raise RuntimeError("unreachable")
