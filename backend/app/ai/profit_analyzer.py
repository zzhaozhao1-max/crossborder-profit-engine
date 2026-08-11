"""
AI Profit Analyzer foundation.
Analyzes profit changes and generates structured business insights.
"""


def analyze_profit_change(current, previous):
    result = {
        "change": 0,
        "reasons": [],
        "suggestions": []
    }

    if previous.get("profit", 0):
        change = (current.get("profit", 0) - previous.get("profit", 0)) / previous["profit"]
        result["change"] = round(change * 100, 2)

    if current.get("ads_cost", 0) > previous.get("ads_cost", 0):
        result["reasons"].append("Advertising cost increased")
        result["suggestions"].append("Review advertising ROI")

    if current.get("refund_rate", 0) > previous.get("refund_rate", 0):
        result["reasons"].append("Refund rate increased")
        result["suggestions"].append("Optimize product quality and listing")

    if current.get("exchange_rate_change"):
        result["reasons"].append("Currency fluctuation affected profit")

    return result
