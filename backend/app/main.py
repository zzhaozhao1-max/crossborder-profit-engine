from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CrossBorder Profit Engine API",
    version="0.1.0"
)


class ProfitRequest(BaseModel):
    selling_price: float
    product_cost: float
    shipping_cost: float = 0
    platform_fee: float = 0
    advertising_cost: float = 0


@app.get("/")
def health_check():
    return {"status": "ok", "service": "CrossBorder Profit Engine"}


@app.post("/api/profit/calculate")
def calculate_profit(data: ProfitRequest):
    revenue = data.selling_price
    total_cost = (
        data.product_cost
        + data.shipping_cost
        + data.platform_fee
        + data.advertising_cost
    )
    profit = revenue - total_cost
    margin = profit / revenue if revenue else 0

    return {
        "revenue": revenue,
        "total_cost": total_cost,
        "profit": round(profit, 2),
        "profit_margin": round(margin * 100, 2)
    }
