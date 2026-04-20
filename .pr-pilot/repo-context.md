Repository: pr-rocket-demo | Primary language: Python

## Architecture Overview
This repository, `pr-rocket-demo`, serves as an end-to-end testing ground for the PR Rocket system (see `README.md:L3`). Its primary purpose is to simulate various PR scenarios to validate PR Rocket's features, such as automated CI fixes and merge conflict resolution (`README.md:L11-L12`). The project itself is a minimal Python application, comprising a simple module (`hello.py`) and its corresponding unit tests (`test_hello.py`), designed to be a target for external automation rather than a standalone functional application.

## Code Style & Conventions
- **Python:** No explicit code style configuration files (e.g., `pyproject.toml`, `.pylintrc`) were found. Standard Python conventions (PEP 8) are implicitly expected.
- **Docstrings:** Functions in `hello.py` include docstrings (`hello.py:L4`, `hello.py:L9`), indicating a convention for documenting code.

## Key Directories & Entry Points
| Directory | Why it matters |
|-----------|----------------|
| `.` | Root directory containing the minimal Python application and tests. |
| `hello.py` | Main application logic, defining `greet` and `add` functions; includes a `if __name__ == "__main__":` block for direct execution (`hello.py:L13`). |
| `test_hello.py` | Contains unit tests for `hello.py` functions, using `assert` statements (`test_hello.py:L5-L10`). |

## Quick Recipes
| Command | Description |
|---------|-------------|
| Run `hello.py` | `python hello.py` |
| Run tests | `python -m pytest test_hello.py` (assuming `pytest` is installed) |

## Dependencies & Compatibility
- **Runtime:** No external runtime dependencies beyond standard Python libraries are explicitly declared or imported, other than `hello` itself being imported by `test_hello.py` (`test_hello.py:L2`).
- **Toolchain:** Python 3 is implied by the syntax (e.g., f-strings in `hello.py:L5`).
- **Observability:** Unknown. No explicit logging, metrics, or tracing libraries are used.

## Unique Workflows
- **PR Rocket Integration:** The repository is configured to trigger PR Rocket webhooks and its associated sandbox/agent pipeline upon opening pull requests (`README.md:L7`). This is the core "workflow" of the repository.
- **Test Scenarios:** Specific PR scenarios are outlined for testing PR Rocket features, including failing CI, merge conflicts, and `/rocket` commands in PR comments (`README.md:L11-L13`).

## API Surface Map
- **Internal Python Functions:** The primary "API" consists of the `greet(name: str) -> str` and `add(a: int, b: int) -> int` functions defined in `hello.py`. These are simple, self-contained functions.
- **Where to learn more:** See `hello.py` for function definitions and `test_hello.py` for usage examples.

## Onboarding Steps
- Understand the purpose of the repository as an e2e test target for PR Rocket (`README.md:L5-L7`).
- Familiarize yourself with the test scenarios outlined in `README.md:L11-L14` to understand expected PR Rocket interactions.
- Review `hello.py` and `test_hello.py` to grasp the minimal Python application structure.

## Getting Unstuck
- For general context on the repository's purpose and test scenarios, refer to the `README.md`.
- If encountering issues related to PR Rocket features, consult the PR Rocket documentation (linked in `README.md:L3`).