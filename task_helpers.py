"""Helpers for working with task lists."""

from typing import Iterable


def group_by_status(tasks: Iterable[dict]) -> dict[str, list[dict]]:
    """Group tasks by their status field. Tasks without a status go to 'unknown'."""
    groups: dict[str, list[dict]] = {}
    for task in tasks:
        status = task.get("status", "unknown")
        groups.setdefault(status, []).append(task)
    return groups


def filter_by_assignee(tasks: Iterable[dict], assignee: str) -> list[dict]:
    """Return tasks whose 'assignee' field matches the given login."""
    return [t for t in tasks if t.get("assignee") == assignee]
