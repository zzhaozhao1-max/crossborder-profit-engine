"""TikTok Shop Excel parser foundation."""


def detect_tiktok_columns(headers):
    keywords = ["订单", "order", "SKU", "商品"]
    text = " ".join(str(x) for x in headers).lower()
    return any(k.lower() in text for k in keywords)


def parse_orders(rows):
    return [{"source": "tiktok", "raw": row} for row in rows]
