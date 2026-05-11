---
name: readme-smoke
blocking: false
paths:
  - README.md
---

Review this diff only for obvious README and markdown problems.

Flag:
- claim-evidence mismatches between the PR title/body and the actual README diff
- accidental stray characters or broken markdown
- misleading user-facing instructions introduced by the change

Do not invent implementation concerns when the diff only touches documentation.
