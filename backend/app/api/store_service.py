"""Store API service layer."""


def list_stores(user_id=None):
    return []


def create_store(name, platform, country, currency):
    return {
        "name": name,
        "platform": platform,
        "country": country,
        "currency": currency,
    }
