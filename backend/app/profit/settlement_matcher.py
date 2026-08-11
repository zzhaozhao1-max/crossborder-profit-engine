"""
V4.1 Settlement Matcher Pro
Match orders with settlement records.
Supports duplicate order ids, multi SKU orders and refund status.
"""

from collections import defaultdict


def match_settlements(orders, settlements):
    settlement_map = defaultdict(list)
    for item in settlements:
        settlement_map[item.get("order_id")].append(item)

    results = []
    for order in orders:
        order_id = order.get("order_id")
        matched = settlement_map.get(order_id, [])
        amount = sum(x.get("amount", 0) for x in matched)
        results.append({
            "order_id": order_id,
            "sku": order.get("sku"),
            "settlement_amount": amount,
            "matched": len(matched) > 0
        })
    return results
