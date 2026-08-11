"""Profit dashboard API service.

Provides dashboard data aggregation entry points.
"""


def get_dashboard_summary(store_id=None):
    return {
        "store_id": store_id,
        "revenue": 0,
        "profit": 0,
        "margin": 0,
        "orders": 0,
    }
