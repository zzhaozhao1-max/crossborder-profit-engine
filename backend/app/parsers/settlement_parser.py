"""Settlement parser foundation."""


def match_order_settlement(orders, settlements):
    result = []
    settlement_map = {str(x.get('order_id')): x for x in settlements}
    for order in orders:
        oid = str(order.get('order_id'))
        result.append({**order, "settlement": settlement_map.get(oid)})
    return result
