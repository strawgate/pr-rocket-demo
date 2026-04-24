# PR Rocket Demo

A test repository for end-to-end testing of [PR Rocket](https://github.com/strawgate/pr-pilot).

## Purpose

This repo exists solely for e2e testing. PRs opened here trigger the PR Rocket webhook → sandbox → agent pipeline.

## Test Scenarios

- Open a PR with a failing lint/test → verify `fix_ci` feature
- Open a PR with merge conflicts → verify `fix_conflicts` feature
- Use `/rocket` commands in PR comments
- Test the control panel toggle flow
- Refresh PR title/body after a docs-only change
