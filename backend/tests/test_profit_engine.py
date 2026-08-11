"""Tests for CrossBorder Profit Engine."""

from app.calculator.profit_engine import calculate_profit


def test_basic_profit_calculation():
    result = calculate_profit(
        selling_price=100,
        product_cost=30,
        shipping_cost=10,
        platform_fee=15,
        advertising_cost=5,
    )

    assert result["profit"] == 40
    assert result["profit_margin"] == 40
