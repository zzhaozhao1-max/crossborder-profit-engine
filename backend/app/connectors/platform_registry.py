"""Marketplace connector registry."""

CONNECTORS = {
    "amazon": {
        "name": "Amazon",
        "status": "planned"
    },
    "tiktok_shop": {
        "name": "TikTok Shop",
        "status": "planned"
    },
    "shopee": {
        "name": "Shopee",
        "status": "planned"
    },
    "walmart": {
        "name": "Walmart",
        "status": "planned"
    }
}


def get_connector(platform):
    return CONNECTORS.get(platform)
