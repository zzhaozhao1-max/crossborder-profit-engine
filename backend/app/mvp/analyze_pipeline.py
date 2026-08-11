"""V5.1 MVP real profit analysis pipeline."""

from dataclasses import dataclass


@dataclass
class AnalysisResult:
    revenue: float = 0
    cost: float = 0
    profit: float = 0
    margin: float = 0


def run_analysis(order_rows=None, settlement_rows=None, cost_map=None):
    """Connect parser, settlement matcher and profit engine."""
    order_rows = order_rows or []
    cost_map = cost_map or {}

    revenue = sum(float(row.get("revenue", 0)) for row in order_rows)
    cost = sum(float(cost_map.get(row.get("sku"), 0)) for row in order_rows)
    profit = revenue - cost

    return AnalysisResult(
        revenue=revenue,
        cost=cost,
        profit=profit,
        margin=(profit / revenue if revenue else 0),
    )
