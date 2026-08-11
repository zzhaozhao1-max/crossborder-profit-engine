"""SKU level profit calculation engine."""


def calculate_sku_profit(revenue, cost, platform_fee=0, ads_cost=0, refund_loss=0):
    total_cost = cost + platform_fee + ads_cost + refund_loss
    profit = revenue - total_cost
    margin = profit / revenue if revenue else 0

    return {
        "revenue": revenue,
        "cost": total_cost,
        "profit": profit,
        "margin": margin,
    }
