"""Simple LRU cache with TTL support."""

import time
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CacheEntry:
    value: Any
    expires_at: float


class TTLCache:
    """Thread-unsafe LRU cache with per-key TTL."""

    def __init__(self, max_size: int = 128, default_ttl: float = 300.0):
        self._max_size = max_size
        self._default_ttl = default_ttl
        self._store: OrderedDict[str, CacheEntry] = OrderedDict()

    def get(self, key: str) -> Any | None:
        entry = self._store.get(key)
        if entry is None:
            return None
        if time.time() > entry.expires_at:
            del self._store[key]
            return None
        self._store.move_to_end(key)
        return entry.value

    def set(self, key: str, value: Any, ttl: float | None = None) -> None:
        if key in self._store:
            del self._store[key]
        elif len(self._store) >= self._max_size:
            self._store.popitem(last=False)
        expires_at = time.time() + (ttl if ttl is not None else self._default_ttl)
        self._store[key] = CacheEntry(value=value, expires_at=expires_at)

    def invalidate(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False

    @property
    def size(self) -> int:
        return len(self._store)
