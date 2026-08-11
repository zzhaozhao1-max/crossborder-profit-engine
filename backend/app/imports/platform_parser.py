"""Marketplace file parser routing layer."""


def detect_platform(columns: list[str]):
    text = ' '.join(columns).lower()
    if 'amazon' in text or 'asin' in text:
        return 'Amazon'
    if 'tiktok' in text:
        return 'TikTok Shop'
    if 'shopee' in text:
        return 'Shopee'
    if 'walmart' in text:
        return 'Walmart'
    return 'Unknown'


def parse_import(columns: list[str]):
    return {
        "platform": detect_platform(columns),
        "columns": columns
    }
