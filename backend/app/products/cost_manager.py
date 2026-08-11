"""SKU cost management module for CrossBorder Profit Engine."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class SKUCost:
    sku: str
    product_cost: float
    shipping_cost: float = 0
    packaging_cost: float = 0

    @property
    def total_cost(self):
        return self.product_cost + self.shipping_cost + self.packaging_cost


class CostManager:
    def __init__(self):
        self.costs: Dict[str, SKUCost] = {}

    def add_cost(self, cost: SKUCost):
        self.costs[cost.sku] = cost

    def get_cost(self, sku: str):
        return self.costs.get(sku)
