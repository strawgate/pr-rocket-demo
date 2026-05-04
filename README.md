# PR Rocket Demo

A test repository for end-to-end testing of [PR Rocket](https://github.com/strawgate/pr-pilot).

## Purpose

This repo exists solely for e2e testing. PRs opened here exercise the PR Rocket webhook → sandbox → agent pipeline from the main branch side and from merge-conflict drills.

## Test Scenarios

- Open a PR with a failing lint/test → verify `fix_ci` feature
- Open a PR with merge conflicts → verify `fix_conflicts` feature
- Use `/rocket` commands in PR comments
- Test the control panel toggle flow using both slash commands and inline status updates

## Build Exercise

We are progressively turning this demo into a tiny task app with PR Rocket.
Step 1 focuses on a small in-memory task manager API and tests.
Step 2 adds a small CLI and JSON persistence on top of that task manager.

## Task CLI Usage

```bash
# Add a task
python task_cli.py add "Buy milk"
python task_cli.py add "Write report" --description "Q2 summary"

# List all tasks
python task_cli.py list

# Filter by status: pending, in_progress, done
python task_cli.py list --status pending

# Complete a task
python task_cli.py complete 1

# Delete a task
python task_cli.py delete 2

# Use a custom store file
python task_cli.py --file my_tasks.json list
```

Tasks are persisted to `tasks.json` in the working directory by default. Use `--file PATH` to specify a different store.

## Development

```bash
pip install -r requirements.txt
python -m pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request
