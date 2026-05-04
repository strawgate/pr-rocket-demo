"""Application metrics collector."""

import time
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Metrics:
    """Collects counters and timing data."""
    _counters: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    _timings: dict[str, list[float]] = field(default_factory=lambda: defaultdict(list))

    def increment(self, name: str, value: int = 1) -> None:
        self._counters[name] += value

    def time(self, name: str):
        """Context manager for timing a block."""
        class Timer:
            def __enter__(timer_self):
                timer_self.start = time.monotonic()
                return timer_self
            def __exit__(timer_self, *args):
                elapsed = time.monotonic() - timer_self.start
                self._timings[name].append(elapsed)
        return Timer()

    def get_counter(self, name: str) -> int:
        return self._counters[name]

    def get_avg_timing(self, name: str) -> float:
        timings = self._timings[name]
        return sum(timings) / len(timings) if timings else 0.0
