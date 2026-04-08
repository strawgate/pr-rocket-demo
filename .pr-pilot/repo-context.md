Repository: pr-rocket-demo | Primary language: Python

## Architecture Overview
This repository serves as an end-to-end testing ground for the external "PR Rocket" system, as detailed in the [README.md](README.md:L3-L7). Its primary function is to simulate various PR scenarios (e.g., failing CI, merge conflicts) to trigger and validate the PR Rocket webhook, sandbox, and agent pipeline. The codebase is minimal, consisting of a simple Python module (`hello.py`) and its corresponding tests (`test_hello.py`), designed to provide basic functionality for these test scenarios.

## Code Style & Conventions
- **Python:** No explicit linter, formatter, or type-checker configurations (e.g., `pyproject.toml`, `.eslintrc`, `mypy.ini`) were found. Code adheres to standard Python syntax and practices.
- **Git:** The `.gitignore` file specifies common Python-related exclusions: `__pycache__/`, `*.pyc`, and `.env` (see [.gitignore](.gitignore)).

## Key Directories & Entry Points
| Directory | Why it matters |
|-----------|----------------|
| `.` (root) | Contains the primary application logic (`hello.py`) and its tests (`test_hello.py`). |
| `hello.py` | Main application module; defines `greet` and `add` functions, with a `__main__` block for direct execution (see [hello.py:L13-L14](hello.py:L13-L14)). |
| `test_hello.py` | Contains unit tests for the `hello.py` module, importing `greet` and `add` (see [test_hello.py:L2](test_hello.py:L2)). |

## Quick Recipes
| Command | Description |
|---------|-------------|
| Run | `python hello.py` (executes the `greet("world")` example) |
| Test | `pytest test_hello.py` (requires `pytest` to be installed; inferred from `test_hello.py` naming convention) |
| Test (specific) | `pytest test_hello.py::test_greet` (runs only the `test_greet` function) |

## Dependencies & Compatibility
- **Runtime:** Python 3.x is the implied language version, given the syntax (e.g., f-strings, type hints in [hello.py](hello.py)).
- **Testing:** `pytest` is the assumed testing framework, based on the `test_*.py` file naming convention and function prefixes (e.g., `test_greet` in [test_hello.py](test_hello.py)). No explicit `requirements.txt` or `pyproject.toml` was found to list dependencies.
- **Observability:** Unknown. No explicit logging, metrics, or tracing libraries/patterns were identified. Next Step: Search for common Python logging/metrics libraries.

## Unique Workflows
- **E2E Testing Trigger:** The core workflow involves opening Pull Requests in this repository to trigger an external "PR Rocket" webhook, which then initiates a sandbox and agent pipeline for end-to-end testing (see [README.md:L7](README.md:L7)).
- **Scenario-based Testing:** The repository is designed to test specific PR Rocket features by simulating scenarios like failing CI, merge conflicts, and `/rocket` commands in PR comments (see [README.md:L11-L14](README.md:L11-L14)).

## API Surface Map
- **Internal Python API:** The primary internal API consists of the `greet(name: str) -> str` and `add(a: int, b: int) -> int` functions within `hello.py`.
- **External API:** The repository itself does not expose an API. Its interaction is outbound, triggering an external "PR Rocket" webhook.
- **Where to learn more:** See [hello.py](hello.py) for function definitions.

## Onboarding Steps
- Understand the purpose of the repository as an e2e testbed for PR Rocket by reviewing the [README.md](README.md).
- Familiarize yourself with the simple Python functions in [hello.py](hello.py) and their corresponding tests in [test_hello.py](test_hello.py).
- **Gotcha:** The project lacks explicit dependency management files (e.g., `requirements.txt`, `pyproject.toml`), so `pytest` must be installed manually (e.g., `pip install pytest`) to run tests.

## Getting Unstuck
- For general understanding of the repository's purpose and how it integrates with the PR Rocket system, refer to the [README.md](README.md).
- If encountering issues with testing, ensure `pytest` is installed in your Python environment.