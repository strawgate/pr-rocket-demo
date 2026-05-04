"""JSON schema validation (minimal implementation)."""

from typing import Any


class ValidationError(Exception):
    def __init__(self, path: str, message: str):
        self.path = path
        super().__init__(f"{path}: {message}")


def validate(data: Any, schema: dict) -> list[ValidationError]:
    """Validate data against a JSON-schema-like dict. Returns list of errors."""
    errors = []
    _validate_node(data, schema, "", errors)
    return errors


def _validate_node(data: Any, schema: dict, path: str, errors: list) -> None:
    expected_type = schema.get("type")
    if expected_type:
        type_map = {"string": str, "integer": int, "number": (int, float),
                    "boolean": bool, "array": list, "object": dict}
        if expected_type in type_map and not isinstance(data, type_map[expected_type]):
            errors.append(ValidationError(path or "$", f"expected {expected_type}, got {type(data).__name__}"))
            return

    if expected_type == "object" and isinstance(data, dict):
        required = schema.get("required", [])
        for field in required:
            if field not in data:
                errors.append(ValidationError(f"{path}.{field}" if path else field, "required field missing"))
        props = schema.get("properties", {})
        for key, sub_schema in props.items():
            if key in data:
                _validate_node(data[key], sub_schema, f"{path}.{key}" if path else key, errors)

    if expected_type == "array" and isinstance(data, list):
        items_schema = schema.get("items")
        if items_schema:
            for i, item in enumerate(data):
                _validate_node(item, items_schema, f"{path}[{i}]", errors)
