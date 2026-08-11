"""
Report Generator V2.7
Generate business reports from profit analysis results.
"""

from datetime import datetime


def generate_summary_report(data: dict):
    return {
        "generated_at": datetime.utcnow().isoformat(),
        "revenue": data.get("revenue", 0),
        "profit": data.get("profit", 0),
        "margin": data.get("margin", 0),
        "top_products": data.get("top_products", []),
    }


def generate_platform_report(platform_data: list):
    return {
        "platforms": platform_data,
        "count": len(platform_data)
    }
