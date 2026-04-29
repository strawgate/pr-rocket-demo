"""Utility functions."""


def sanitize_input(text: str) -> str:
    """Remove dangerous characters from user input."""
    return text.replace("<", "&lt;").replace(">", "&gt;")


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format a number as currency."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:.2f}"
