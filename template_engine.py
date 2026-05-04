"""Minimal template engine."""

import re
from typing import Any


class TemplateError(Exception):
    pass


def render(template: str, context: dict[str, Any]) -> str:
    """Render template with variable substitution."""
    def replacer(match):
        key = match.group(1).strip()
        if key not in context:
            raise TemplateError(f"Undefined variable: {key}")
        return str(context[key])
    return re.sub(r"\{\{\s*(\w+)\s*\}\}", replacer, template)
