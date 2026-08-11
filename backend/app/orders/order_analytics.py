"""
Order Analytics Engine

Core module for cross-border order and settlement analysis.

Planned features:
- Import marketplace order files
- Match payment records
- Remove duplicate SKU settlement records
- Calculate valid sales quantity
- Analyze refunds and net revenue
"""


def calculate_order_summary(orders):
    """Basic order summary calculation.

    orders example:
    [
        {
            "sku": "SKU001",
            "amount": 100,
            "refund": 0
        }
    ]
    """
    total_orders = len(orders)
    total_sales = sum(item.get("amount", 0) for item in orders)
    total_refund = sum(item.get("refund", 0) for item in orders)

    return {
        "total_orders": total_orders,
        "gross_sales": total_sales,
        "refund_amount": total_refund,
        "net_sales": total_sales - total_refund,
    }
