"""Tests for task_cli.py and task_store.py."""

import pytest
from pathlib import Path

from task_manager import TaskManager, TaskStatus
from task_store import load, save
from task_cli import main


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def store(tmp_path) -> Path:
    """Return a path to a temporary task store that does not yet exist."""
    return tmp_path / "tasks.json"


# ---------------------------------------------------------------------------
# task_store — persistence
# ---------------------------------------------------------------------------


def test_load_missing_file_returns_empty(store):
    manager = load(store)
    assert manager.list_tasks() == []


def test_save_and_load_roundtrip(store):
    manager = TaskManager()
    manager.add_task("Buy milk", description="Whole milk")
    t2 = manager.add_task("Walk dog")
    manager.complete_task(t2.id)

    save(manager, store)
    loaded = load(store)

    tasks = loaded.list_tasks()
    assert len(tasks) == 2
    assert {t.title for t in tasks} == {"Buy milk", "Walk dog"}


def test_save_persists_status(store):
    manager = TaskManager()
    task = manager.add_task("Do laundry")
    manager.complete_task(task.id)
    save(manager, store)

    loaded = load(store)
    assert loaded.get_task(task.id).status == TaskStatus.DONE


def test_save_persists_description(store):
    manager = TaskManager()
    manager.add_task("Research", description="Look up references")
    save(manager, store)

    loaded = load(store)
    assert loaded.list_tasks()[0].description == "Look up references"


def test_save_preserves_next_id(store):
    """IDs must not restart after a round-trip (avoids collisions)."""
    manager = TaskManager()
    t = manager.add_task("First")
    manager.delete_task(t.id)
    save(manager, store)

    loaded = load(store)
    new_task = loaded.add_task("Second")
    assert new_task.id == 2


# ---------------------------------------------------------------------------
# CLI — add
# ---------------------------------------------------------------------------


def test_cli_add_prints_confirmation(store, capsys):
    main(["--file", str(store), "add", "Fix bug"])
    out = capsys.readouterr().out
    assert "Fix bug" in out
    assert "Added" in out


def test_cli_add_persists_task(store):
    main(["--file", str(store), "add", "Persisted task"])
    loaded = load(store)
    assert any(t.title == "Persisted task" for t in loaded.list_tasks())


def test_cli_add_with_description(store):
    main(["--file", str(store), "add", "Research", "--description", "Check docs"])
    loaded = load(store)
    task = loaded.list_tasks()[0]
    assert task.description == "Check docs"


# ---------------------------------------------------------------------------
# CLI — list
# ---------------------------------------------------------------------------


def test_cli_list_empty(store, capsys):
    main(["--file", str(store), "list"])
    assert "No tasks found" in capsys.readouterr().out


def test_cli_list_shows_tasks(store, capsys):
    main(["--file", str(store), "add", "Task A"])
    main(["--file", str(store), "add", "Task B"])
    main(["--file", str(store), "list"])
    out = capsys.readouterr().out
    assert "Task A" in out
    assert "Task B" in out


def test_cli_list_filter_pending(store, capsys):
    main(["--file", str(store), "add", "Pending task"])
    main(["--file", str(store), "add", "Done task"])
    main(["--file", str(store), "complete", "2"])
    capsys.readouterr()  # discard setup output
    main(["--file", str(store), "list", "--status", "pending"])
    out = capsys.readouterr().out
    assert "Pending task" in out
    assert "Done task" not in out


def test_cli_list_filter_done(store, capsys):
    main(["--file", str(store), "add", "Pending task"])
    main(["--file", str(store), "add", "Done task"])
    main(["--file", str(store), "complete", "2"])
    capsys.readouterr()  # discard setup output
    main(["--file", str(store), "list", "--status", "done"])
    out = capsys.readouterr().out
    assert "Done task" in out
    assert "Pending task" not in out


# ---------------------------------------------------------------------------
# CLI — complete
# ---------------------------------------------------------------------------


def test_cli_complete_prints_confirmation(store, capsys):
    main(["--file", str(store), "add", "Deploy app"])
    main(["--file", str(store), "complete", "1"])
    out = capsys.readouterr().out
    assert "Completed" in out
    assert "Deploy app" in out
    assert "done" in out.lower()


def test_cli_complete_persists_status(store):
    main(["--file", str(store), "add", "Deploy app"])
    main(["--file", str(store), "complete", "1"])
    loaded = load(store)
    assert loaded.get_task(1).status == TaskStatus.DONE


def test_cli_complete_missing_id_prints_error(store, capsys):
    main(["--file", str(store), "complete", "99"])
    out = capsys.readouterr().out
    assert "not found" in out.lower() or "error" in out.lower()


# ---------------------------------------------------------------------------
# CLI — delete
# ---------------------------------------------------------------------------


def test_cli_delete_removes_task(store):
    main(["--file", str(store), "add", "To delete"])
    main(["--file", str(store), "delete", "1"])
    loaded = load(store)
    assert loaded.list_tasks() == []


def test_cli_delete_prints_confirmation(store, capsys):
    main(["--file", str(store), "add", "Temp task"])
    capsys.readouterr()
    main(["--file", str(store), "delete", "1"])
    out = capsys.readouterr().out
    assert "Deleted" in out
    assert "1" in out


def test_cli_delete_missing_id_prints_error(store, capsys):
    main(["--file", str(store), "delete", "99"])
    out = capsys.readouterr().out
    assert "not found" in out.lower() or "error" in out.lower()
