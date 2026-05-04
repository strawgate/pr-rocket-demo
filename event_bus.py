"""Simple event bus for decoupled components."""

from collections import defaultdict
from typing import Any, Callable


class EventBus:
    """Pub/sub event system."""

    def __init__(self):
        self._handlers: dict[str, list[Callable]] = defaultdict(list)

    def on(self, event: str, handler: Callable) -> None:
        """Subscribe to an event."""
        self._handlers[event].append(handler)

    def off(self, event: str, handler: Callable) -> None:
        """Unsubscribe from an event."""
        self._handlers[event] = [h for h in self._handlers[event] if h != handler]

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Emit an event, calling all registered handlers."""
        for handler in self._handlers.get(event, []):
            handler(*args, **kwargs)

    def once(self, event: str, handler: Callable) -> None:
        """Subscribe to an event for a single invocation."""
        def wrapper(*args, **kwargs):
            handler(*args, **kwargs)
            self.off(event, wrapper)
        self.on(event, wrapper)

    @property
    def event_names(self) -> list[str]:
        """List all events with registered handlers."""
        return [k for k, v in self._handlers.items() if v]
