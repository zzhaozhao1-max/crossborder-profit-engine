"""
Marketplace Fee Engine V0.1

Basic fee model for cross-border marketplaces.
Future versions will support platform-specific rules.
"""


def calculate_platform_fee(sales_price: float, fee_rate: float) -> float:
    """Calculate marketplace commission."""
    return round(sales_price * fee_rate, 2)


def calculate_creator_commission(sales_price: float, commission_rate: float) -> float:
    """Calculate influencer/creator commission."""
    return round(sales_price * commission_rate, 2)


def calculate_total_platform_cost(
    sales_price: float,
    platform_fee_rate: float = 0,
    creator_rate: float = 0,
    advertising_cost: float = 0,
):
    """Calculate total marketplace related costs."""
    platform_fee = calculate_platform_fee(sales_price, platform_fee_rate)
    creator_fee = calculate_creator_commission(sales_price, creator_rate)

    return {
        "platform_fee": platform_fee,
        "creator_fee": creator_fee,
        "advertising_cost": advertising_cost,
        "total_marketplace_cost": round(
            platform_fee + creator_fee + advertising_cost, 2
        ),
    }
