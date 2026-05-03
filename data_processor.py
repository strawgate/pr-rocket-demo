"""Data processing pipeline with validation and transformation."""

import json
from datetime import datetime
from typing import Any


class DataProcessor:
    """Process and validate incoming data records."""

    def __init__(self, schema: dict[str, type]):
        self._schema = schema
        self._processed = 0
        self._errors: list[str] = []

    def validate(self, record: dict[str, Any]) -> bool:
        """Check record matches expected schema."""
        for field, expected_type in self._schema.items():
            if field not in record:
                self._errors.append(f"Missing field: {field}")
                return False
            if not isinstance(record[field], expected_type):
                self._errors.append(f"Type mismatch: {field}")
                return False
        return True

    def transform(self, record: dict[str, Any]) -> dict[str, Any]:
        """Add metadata and normalize fields."""
        result = dict(record)
        result["processed_at"] = datetime.utcnow().isoformat()
        result["version"] = 2
        if "name" in result:
            result["name"] = result["name"].strip().title()
        return result

    def process_batch(self, records: list[dict]) -> list[dict]:
        """Process a batch of records, skipping invalid ones."""
        results = []
        for record in records:
            if self.validate(record):
                results.append(self.transform(record))
                self._processed += 1
        return results

    def get_stats(self) -> dict:
        return {"processed": self._processed, "errors": len(self._errors)}

    def export_json(self, records: list[dict], path: str) -> None:
        """Export processed records to JSON file."""
        with open(path, "w") as f:
            json.dump(records, f, indent=2, default=str)
