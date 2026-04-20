| | Finding | Location |
|---|---------|----------|
| 🔴 | `test_greet` was failing — expected `"Hello, world!"` but function returns `"Hi there, world!"` | `test_hello.py:7` |
| 🟢 | `TaskManager` implements full CRUD: `add_task`, `get_task`, `list_tasks`, `update_task`, `complete_task`, `delete_task` | `task_manager.py` |
| 🟢 | `TaskNotFoundError` raised consistently for missing IDs | `task_manager.py:28` |
| 🟢 | 17 tests cover all `TaskManager` methods including edge cases | `test_task_manager.py` |
| ℹ️ | `TaskStatus` uses `str, Enum` so values serialise cleanly as strings | `task_manager.py:11` |
