"""
Currency Engine V0.1

Base currency: CNY
Supported markets:
- USD
- VND
- PHP
- MYR
- THB

Rates are configurable and should be updated from reliable exchange rate sources.
"""

DEFAULT_RATES = {
    "USD": 6.77,
    "VND": 0.000258,
    "PHP": 0.1098,
    "MYR": 1.58,
    "THB": 0.209,
}


def convert_to_cny(amount: float, currency: str) -> float:
    """Convert foreign currency amount to CNY."""
    rate = DEFAULT_RATES.get(currency.upper())
    if not rate:
        raise ValueError(f"Unsupported currency: {currency}")
    return round(amount * rate, 2)
