# PR Rocket Auto-Pilot Summary

## Event processed
`/rocket enable auto-pilot` — activated full auto-pilot mode.

## PR Goal
Build a simple in-memory task manager library (Step 1 of the progressive build exercise).

## Actions taken

### 1. Fixed failing test — `test_hello.py:7`
The `greet` function was updated in a prior refactor (`refactor: update greeting message`) to return `"Hi there, {name}!"`, but the test still expected `"Hello, world!"`.

**Before:**
```python
assert greet("world") == "Hello, world!"
```
**After:**
```python
assert greet("world") == "Hi there, world!"
```

### 2. Created `task_manager.py`
New in-memory task manager library with:

| Symbol | Purpose |
|--------|---------|
| `TaskStatus` (Enum) | `PENDING`, `IN_PROGRESS`, `DONE` |
| `Task` (dataclass) | Fields: `id`, `title`, `description`, `status` |
| `TaskNotFoundError` | Raised by all operations on missing IDs |
| `TaskManager.add_task` | Creates & stores a new task; returns it |
| `TaskManager.get_task` | Returns task by ID or raises `TaskNotFoundError` |
| `TaskManager.list_tasks` | Returns all tasks, optionally filtered by status |
| `TaskManager.update_task` | Updates title/description/status; returns task |
| `TaskManager.complete_task` | Convenience wrapper: sets status to DONE |
| `TaskManager.delete_task` | Removes task from store |

### 3. Created `test_task_manager.py`
17 tests covering all public methods including:
- Happy paths (add, get, list, update, complete, delete)
- Status filtering in `list_tasks`
- `TaskNotFoundError` raised for every operation on missing IDs
- `delete_task` only removes the targeted task

## Verification
```
19 passed in 0.04s
```
All tests (2 existing + 17 new) pass.
