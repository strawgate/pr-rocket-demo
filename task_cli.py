#!/usr/bin/env python3
"""CLI for managing tasks from the terminal."""

import argparse
from pathlib import Path

from task_manager import TaskNotFoundError, TaskStatus
from task_store import DEFAULT_PATH, load, save


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------


def cmd_list(args: argparse.Namespace, manager) -> None:
    """List tasks, optionally filtered by status."""
    status = TaskStatus(args.status) if args.status else None
    tasks = manager.list_tasks(status=status)
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        desc = f"  {task.description}" if task.description else ""
        print(f"[{task.id}] [{task.status.value}] {task.title}{desc}")


def cmd_add(args: argparse.Namespace, manager) -> None:
    """Add a new task."""
    task = manager.add_task(args.title, description=args.description or "")
    print(f"Added task [{task.id}]: {task.title}")


def cmd_complete(args: argparse.Namespace, manager) -> None:
    """Mark a task as done."""
    try:
        task = manager.complete_task(args.id)
    except TaskNotFoundError:
        print(f"Error: task {args.id} not found.")
        return
    print(f"Completed task [{task.id}]: {task.title}")


def cmd_delete(args: argparse.Namespace, manager) -> None:
    """Delete a task."""
    try:
        manager.delete_task(args.id)
    except TaskNotFoundError:
        print(f"Error: task {args.id} not found.")
        return
    print(f"Deleted task [{args.id}].")


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Return the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="task",
        description="Manage tasks from the terminal.",
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_PATH,
        metavar="PATH",
        help="Path to the JSON task store (default: tasks.json)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument(
        "--status",
        choices=[s.value for s in TaskStatus],
        help="Filter by status",
    )

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title")
    p_add.add_argument("--description", "-d", default="", help="Optional description")

    # complete
    p_complete = sub.add_parser("complete", help="Mark a task as done")
    p_complete.add_argument("id", type=int, help="Task ID")

    # delete
    p_delete = sub.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id", type=int, help="Task ID")

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv=None) -> None:
    """Parse arguments, run the requested command, and persist changes."""
    parser = build_parser()
    args = parser.parse_args(argv)

    manager = load(args.file)

    handlers = {
        "list": cmd_list,
        "add": cmd_add,
        "complete": cmd_complete,
        "delete": cmd_delete,
    }
    handlers[args.command](args, manager)

    save(manager, args.file)


if __name__ == "__main__":
    main()
