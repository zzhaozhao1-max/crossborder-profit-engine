"""MVP dashboard aggregation service"""


def build_dashboard(result):
    return {
        "revenue": result.get("revenue", 0),
        "cost": result.get("cost", 0),
        "profit": result.get("profit", 0),
        "margin": result.get("margin", 0),
    }
