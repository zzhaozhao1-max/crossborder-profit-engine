"""Settlement matching engine foundation.

Matches marketplace settlement records with normalized orders.
"""


def match_settlement(order, settlement):
    """Basic settlement matching by order id."""
    return order.get("order_id") == settlement.get("order_id")


def calculate_net_income(settlement):
    """Calculate net income after refunds and fees."""
    amount = settlement.get("amount", 0)
    refund = settlement.get("refund", 0)
    fee = settlement.get("fee", 0)
    return amount - refund - fee
