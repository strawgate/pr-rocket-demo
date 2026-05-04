"""Thread-safe bounded queue."""

import threading
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class BoundedQueue(Generic[T]):
    """Thread-safe FIFO queue with max capacity."""

    def __init__(self, max_size: int = 100):
        self._queue: deque[T] = deque()
        self._max_size = max_size
        self._lock = threading.Lock()
        self._not_empty = threading.Condition(self._lock)
        self._not_full = threading.Condition(self._lock)

    def put(self, item: T, timeout: float | None = None) -> bool:
        """Add item to queue. Returns False if full after timeout."""
        with self._not_full:
            if len(self._queue) >= self._max_size:
                if not self._not_full.wait(timeout):
                    return False
            self._queue.append(item)
            self._not_empty.notify()
            return True

    def get(self, timeout: float | None = None) -> T | None:
        """Remove and return item. Returns None if empty after timeout."""
        with self._not_empty:
            if not self._queue:
                if not self._not_empty.wait(timeout):
                    return None
            item = self._queue.popleft()
            self._not_full.notify()
            return item

    @property
    def size(self) -> int:
        with self._lock:
            return len(self._queue)

    @property
    def empty(self) -> bool:
        return self.size == 0
