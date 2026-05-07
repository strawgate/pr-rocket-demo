"""Math helpers for demo flows."""


def clamp_percent(value: float) -> float:
    """Clamp a percentage into the accepted range."""
    if value < 0:
        return 0.0
    if value > 100:
        return 100.0
    return value
