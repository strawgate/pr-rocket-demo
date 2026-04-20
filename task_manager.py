"""In-memory task manager library."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class TaskStatus(str, Enum):
    """Valid statuses for a task."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Task:
    """Represents a single task."""

    id: int
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.PENDING
    priority: str = "medium"


class TaskNotFoundError(KeyError):
    """Raised when a task ID does not exist."""


class TaskManager:
    """Simple in-memory task manager."""

    def __init__(self) -> None:
        """Initialise with an empty task store."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "", priority: str = "medium") -> Task:
        """Create and store a new task, returning it."""
        task = Task(id=self._next_id, title=title, description=description, priority=priority)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """Return the task with *task_id*, or raise TaskNotFoundError."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]

    def list_tasks(self, status: Optional[TaskStatus] = None, priority: Optional[str] = None) -> list[Task]:
        """Return all tasks, optionally filtered by *status* and/or *priority*."""
        tasks = list(self._tasks.values())
        if status is not None:
            tasks = [t for t in tasks if t.status == status]
        if priority is not None:
            tasks = [t for t in tasks if t.priority == priority]
        return tasks

    def update_task(
        self,
        task_id: int,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[TaskStatus] = None,
    ) -> Task:
        """Update fields on an existing task and return it."""
        task = self.get_task(task_id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        return task

    def complete_task(self, task_id: int) -> Task:
        """Mark *task_id* as DONE and return it."""
        return self.update_task(task_id, status=TaskStatus.DONE)

    def delete_task(self, task_id: int) -> None:
        """Remove *task_id* from the store."""
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        del self._tasks[task_id]
