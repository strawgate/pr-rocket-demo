"""E2E validation module — tests PR Rocket production processing.

This file exercises multiple check agent categories:
- test-coverage: has a function without tests
- docs-freshness: references potentially outdated API docs
- input-validation: handles user input without sanitization
"""


def process_user_input(raw_input: str) -> dict:
    """Process raw user input and return structured data.

    TODO: Add input validation and sanitization.
    See: https://docs.example.com/api/v2/input-processing (may be outdated)
    """
    # This intentionally lacks validation for check agent testing
    parts = raw_input.split(",")
    return {
        "name": parts[0],
        "email": parts[1],
        "age": int(parts[2]),
    }


def calculate_metrics(data: list[dict]) -> dict:
    """Calculate aggregate metrics from a dataset."""
    if not data:
        return {"count": 0, "avg": 0.0}

    total = sum(item.get("value", 0) for item in data)
    return {
        "count": len(data),
        "total": total,
        "avg": total / len(data),
    }


# Duplicate logic — should be refactored (tests code-duplication agent)
def calculate_stats(records: list[dict]) -> dict:
    """Calculate stats from records."""
    if not records:
        return {"count": 0, "avg": 0.0}

    total = sum(r.get("value", 0) for r in records)
    return {
        "count": len(records),
        "total": total,
        "avg": total / len(records),
    }
