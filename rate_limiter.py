"""Simple token-bucket rate limiter."""

import time
from dataclasses import dataclass, field


@dataclass
class RateLimiter:
    """Token bucket rate limiter."""
    max_tokens: int = 10
    refill_rate: float = 1.0
    _tokens: float = field(init=False, default=0)
    _last_refill: float = field(init=False, default=0)

    def __post_init__(self):
        self._tokens = float(self.max_tokens)
        self._last_refill = time.monotonic()

    def _refill(self):
        now = time.monotonic()
        elapsed = now - self._last_refill
        self._tokens = min(self.max_tokens, self._tokens + elapsed * self.refill_rate)
        self._last_refill = now

    def acquire(self) -> bool:
        """Try to acquire a token. Returns True if allowed."""
        self._refill()
        if self._tokens >= 1:
            self._tokens -= 1
            return True
        return False

    @property
    def available(self) -> int:
        """Number of tokens currently available."""
        self._refill()
        return int(self._tokens)
