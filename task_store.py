"""JSON persistence for TaskManager."""

import json
from pathlib import Path

from task_manager import Task, TaskManager, TaskStatus

DEFAULT_PATH = Path("tasks.json")


def load(path: Path = DEFAULT_PATH) -> TaskManager:
    """Load a TaskManager from *path*, or return an empty one if the file is absent."""
    manager = TaskManager()
    if not path.exists():
        return manager
    data = json.loads(path.read_text())
    for item in data["tasks"]:
        task = Task(
            id=item["id"],
            title=item["title"],
            description=item.get("description", ""),
            status=TaskStatus(item["status"]),
            tags=item.get("tags", []),
        )
        manager._tasks[task.id] = task
    manager._next_id = data.get(
        "next_id",
        max((t.id for t in manager._tasks.values()), default=0) + 1,
    )
    return manager


def save(manager: TaskManager, path: Path = DEFAULT_PATH) -> None:
    """Persist *manager* state to *path* as JSON."""
    data = {
        "next_id": manager._next_id,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "status": t.status.value,
                "tags": t.tags,
            }
            for t in manager._tasks.values()
        ],
    }
    path.write_text(json.dumps(data, indent=2))
