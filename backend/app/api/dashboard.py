"""Dashboard API foundation for CrossBorder Profit Engine.

Provides summary endpoints structure for future dashboard analytics.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/summary")
def dashboard_summary():
    return {
        "revenue": 0,
        "profit": 0,
        "margin": 0,
        "roi": 0,
        "currency": "USD"
    }


@router.get("/products")
def product_summary():
    return {
        "products": []
    }
