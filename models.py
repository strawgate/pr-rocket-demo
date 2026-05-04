"""Data models for the application."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Task:
    """An immutable task."""
    id: str
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    created_at: datetime = field(default_factory=datetime.now)
    tags: tuple[str, ...] = ()

    @property
    def is_high_priority(self) -> bool:
        return self.priority in (Priority.HIGH, Priority.CRITICAL)


@dataclass(frozen=True)
class TaskList:
    """Collection of tasks with filtering."""
    tasks: tuple[Task, ...] = ()

    def filter_by_priority(self, priority: Priority) -> "TaskList":
        return TaskList(
            tasks=tuple(t for t in self.tasks if t.priority == priority)
        )

    def filter_by_tag(self, tag: str) -> "TaskList":
        return TaskList(
            tasks=tuple(t for t in self.tasks if tag in t.tags)
        )

    @property
    def count(self) -> int:
        return len(self.tasks)
