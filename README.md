# PR Rocket Demo

A test repository for end-to-end testing of [PR Rocket](https://github.com/strawgate/pr-pilot).

## Purpose

This repo exists solely for e2e testing. PRs opened here exercise the PR Rocket webhook → sandbox → agent pipeline from the main branch side and from merge-conflict drills.
It also serves as a safe target for validating production webhook and cache-hydration behavior after PR Rocket deploys.
Small README-only main-branch commits here are expected when validating webhook and cache refresh plumbing.
This line was added to validate the RepoDO repo-context refresh RPC fix on May 9, 2026.

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
x

<!-- pr-rocket-check-agent-smoke:1780279646:972424c0 -->
