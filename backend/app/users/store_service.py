"""Store management service."""


def create_store(name: str, platform: str, country: str, currency: str):
    return {
        "name": name,
        "platform": platform,
        "country": country,
        "currency": currency,
        "active": True,
    }


def list_supported_platforms():
    return [
        "Amazon",
        "TikTok Shop",
        "Shopee",
        "Walmart",
        "Shopify",
    ]
