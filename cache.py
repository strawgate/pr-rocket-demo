"""Simple in-memory cache with TTL."""
import time

class TTLCache:
    def __init__(self, default_ttl=60):
        self._store = {}
        self._ttl = default_ttl

    def get(self, key):
        entry = self._store.get(key)
        if entry and time.time() < entry[1]:
            return entry[0]
        self._store.pop(key, None)
        return None

    def set(self, key, value, ttl=None):
        expires = time.time() + (ttl or self._ttl)
        self._store[key] = (value, expires)

    def clear(self):
        self._store.clear()
