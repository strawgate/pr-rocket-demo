"""Helper utilities for the demo project."""

E2E_RUN_ID = "1779283394"

def calculate_discount(price: float, percent: float) -> float:
    """Apply a percentage discount to a price."""
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)

def format_currency(amount: float, currency: str = "USD") -> str:
    """Format an amount as currency string."""
    symbols = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3"}
    symbol = symbols.get(currency, currency + " ")
    return f"{symbol}{amount:.2f}"
