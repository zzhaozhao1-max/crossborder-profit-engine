"""Profit dashboard aggregation service."""


def build_profit_summary(records=None):
    records = records or []
    revenue = sum(r.get('revenue', 0) for r in records)
    cost = sum(r.get('cost', 0) for r in records)
    profit = revenue - cost
    margin = profit / revenue if revenue else 0
    return {
        'revenue': revenue,
        'cost': cost,
        'profit': profit,
        'margin': margin,
    }
