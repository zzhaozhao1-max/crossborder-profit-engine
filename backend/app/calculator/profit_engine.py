"""
CrossBorder Profit Engine
V0.1 calculation prototype
"""


def calculate_profit(
    selling_price,
    product_cost,
    shipping_cost,
    platform_fee,
    advertising_cost,
    refund_rate=0,
):
    """Calculate basic product profitability."""

    revenue_after_refund = selling_price * (1 - refund_rate)

    total_cost = (
        product_cost
        + shipping_cost
        + platform_fee
        + advertising_cost
    )

    profit = revenue_after_refund - total_cost

    margin = 0
    if selling_price:
        margin = profit / selling_price

    return {
        "revenue": revenue_after_refund,
        "cost": total_cost,
        "profit": profit,
        "profit_margin": margin,
    }
