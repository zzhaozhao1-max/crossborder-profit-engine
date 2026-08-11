"""Order file parser foundation.

Normalizes CSV/XLSX marketplace exports into a unified order structure.
"""

from typing import List, Dict


def normalize_order(row: Dict) -> Dict:
    return {
        "order_id": row.get("order_id") or row.get("Order ID"),
        "sku": row.get("sku") or row.get("SKU"),
        "product_name": row.get("product_name") or row.get("Product Name"),
        "amount": float(row.get("amount") or row.get("Amount") or 0),
        "refund": float(row.get("refund") or row.get("Refund") or 0),
        "currency": row.get("currency") or row.get("Currency") or "USD",
    }


def parse_rows(rows: List[Dict]) -> List[Dict]:
    return [normalize_order(row) for row in rows]
