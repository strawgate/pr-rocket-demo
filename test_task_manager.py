"""Tests for task_manager.py."""

import pytest

from task_manager import Task, TaskManager, TaskNotFoundError, TaskStatus


@pytest.fixture()
def manager() -> TaskManager:
    """Return a fresh TaskManager for each test."""
    return TaskManager()


# ---------------------------------------------------------------------------
# add_task
# ---------------------------------------------------------------------------


def test_add_task_returns_task(manager):
    task = manager.add_task("Buy milk")
    assert isinstance(task, Task)
    assert task.title == "Buy milk"
    assert task.status == TaskStatus.PENDING


def test_add_task_assigns_unique_ids(manager):
    t1 = manager.add_task("Task 1")
    t2 = manager.add_task("Task 2")
    assert t1.id != t2.id


def test_add_task_stores_description(manager):
    task = manager.add_task("Write tests", description="Cover all edge cases")
    assert task.description == "Cover all edge cases"


# ---------------------------------------------------------------------------
# get_task
# ---------------------------------------------------------------------------


def test_get_task_returns_correct_task(manager):
    added = manager.add_task("Fix bug")
    fetched = manager.get_task(added.id)
    assert fetched is added


def test_get_task_raises_for_missing_id(manager):
    with pytest.raises(TaskNotFoundError):
        manager.get_task(999)


# ---------------------------------------------------------------------------
# list_tasks
# ---------------------------------------------------------------------------


def test_list_tasks_empty(manager):
    assert manager.list_tasks() == []


def test_list_tasks_returns_all(manager):
    manager.add_task("A")
    manager.add_task("B")
    assert len(manager.list_tasks()) == 2


def test_list_tasks_filter_by_status(manager):
    t1 = manager.add_task("Pending task")
    t2 = manager.add_task("Done task")
    manager.complete_task(t2.id)

    pending = manager.list_tasks(status=TaskStatus.PENDING)
    done = manager.list_tasks(status=TaskStatus.DONE)

    assert t1 in pending
    assert t2 not in pending
    assert t2 in done
    assert t1 not in done


# ---------------------------------------------------------------------------
# update_task
# ---------------------------------------------------------------------------


def test_update_task_title(manager):
    task = manager.add_task("Old title")
    updated = manager.update_task(task.id, title="New title")
    assert updated.title == "New title"


def test_update_task_description(manager):
    task = manager.add_task("Task", description="old")
    manager.update_task(task.id, description="new description")
    assert task.description == "new description"


def test_update_task_status(manager):
    task = manager.add_task("Task")
    manager.update_task(task.id, status=TaskStatus.IN_PROGRESS)
    assert task.status == TaskStatus.IN_PROGRESS


def test_update_task_raises_for_missing_id(manager):
    with pytest.raises(TaskNotFoundError):
        manager.update_task(42, title="Ghost")


# ---------------------------------------------------------------------------
# complete_task
# ---------------------------------------------------------------------------


def test_complete_task_sets_done(manager):
    task = manager.add_task("Deploy app")
    manager.complete_task(task.id)
    assert task.status == TaskStatus.DONE


def test_complete_task_returns_done_task(manager):
    task = manager.add_task("Validate return value")
    completed = manager.complete_task(task.id)
    assert completed.status == TaskStatus.DONE


def test_complete_task_raises_for_missing_id(manager):
    with pytest.raises(TaskNotFoundError):
        manager.complete_task(99)


# ---------------------------------------------------------------------------
# delete_task
# ---------------------------------------------------------------------------


def test_delete_task_removes_it(manager):
    task = manager.add_task("Temporary")
    manager.delete_task(task.id)
    assert len(manager.list_tasks()) == 0


def test_delete_task_raises_for_missing_id(manager):
    with pytest.raises(TaskNotFoundError):
        manager.delete_task(7)


def test_delete_task_only_removes_target(manager):
    t1 = manager.add_task("Keep me")
    t2 = manager.add_task("Delete me")
    manager.delete_task(t2.id)
    assert manager.get_task(t1.id) is t1
    with pytest.raises(TaskNotFoundError):
        manager.get_task(t2.id)
