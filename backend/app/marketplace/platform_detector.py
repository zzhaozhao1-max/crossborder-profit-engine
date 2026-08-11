"""
Platform and marketplace detector.

Detects marketplace source from uploaded order files.
"""


def detect_platform(columns, filename=""):
    text = " ".join(columns).lower() + " " + filename.lower()

    if "amazon" in text or "asin" in text or "fba" in text:
        return {"platform": "Amazon", "country": "US"}

    if "tiktok" in text or "tik tok" in text:
        return {"platform": "TikTok Shop", "country": "Unknown"}

    if "shopee" in text:
        return {"platform": "Shopee", "country": "Unknown"}

    if "walmart" in text:
        return {"platform": "Walmart", "country": "US"}

    return {"platform": "Unknown", "country": "Unknown"}
