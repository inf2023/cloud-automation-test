"""Exact milk delivery amount calculations in INR."""

from decimal import Decimal


def calculate_milk_delivery_amount(
    quantity_liters: Decimal, rate_per_liter: Decimal
) -> Decimal:
    """Return quantity times rate; pass Decimal values created from strings."""
    return quantity_liters * rate_per_liter
