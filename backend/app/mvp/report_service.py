"""V5.3 report service
Generate analysis report data from completed tasks.
"""


def build_report(task_result: dict) -> dict:
    return {
        "summary": {
            "revenue": task_result.get("revenue", 0),
            "cost": task_result.get("cost", 0),
            "profit": task_result.get("profit", 0),
            "margin": task_result.get("margin", 0),
        },
        "sku_ranking": task_result.get("sku_ranking", []),
        "refund_rate": task_result.get("refund_rate", 0),
        "orders": task_result.get("orders", 0),
    }
