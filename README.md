# PR Rocket Demo

A test repository for end-to-end testing of [PR Rocket](https://github.com/strawgate/pr-pilot).

## Purpose

This repo exists solely for e2e testing. PRs opened here trigger the PR Rocket webhook → sandbox → agent pipeline.

## Test Scenarios

- Open a PR with a failing lint/test → verify `fix_ci` feature
- Open a PR with merge conflicts → verify `fix_conflicts` feature
- Use `/rocket` commands in PR comments
- Test the control panel toggle flow

## Build Exercise

We are progressively turning this demo into a tiny task app with PR Rocket.
Step 1 focuses on a small in-memory task manager API and tests.
Step 2 adds a small CLI and JSON persistence on top of that task manager.
