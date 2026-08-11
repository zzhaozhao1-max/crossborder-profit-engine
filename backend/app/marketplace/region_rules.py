"""
Regional marketplace rule database foundation.

Stores configurable fee rules by marketplace and country.
"""

REGION_RULES = {
    "tiktok_vietnam": {
        "marketplace": "TikTok Shop",
        "country": "Vietnam",
        "currency": "VND",
        "platform_fee_rate": 0.05,
        "affiliate_fee_rate": 0.10,
    },
    "tiktok_thailand": {
        "marketplace": "TikTok Shop",
        "country": "Thailand",
        "currency": "THB",
        "platform_fee_rate": 0.05,
        "affiliate_fee_rate": 0.10,
    },
    "amazon_us": {
        "marketplace": "Amazon",
        "country": "United States",
        "currency": "USD",
        "referral_fee_rate": 0.15,
    },
}


def get_region_rule(region: str):
    return REGION_RULES.get(region)
