"""
Marketplace Fee Rules Engine V2
Support multi-platform fee calculation foundation.
"""


def calculate_tiktok_shop_fee(sales_amount, platform_rate=0.05, affiliate_rate=0, ads_cost=0):
    platform_fee = sales_amount * platform_rate
    affiliate_fee = sales_amount * affiliate_rate
    return {
        "platform_fee": platform_fee,
        "affiliate_fee": affiliate_fee,
        "ads_cost": ads_cost,
        "total_fee": platform_fee + affiliate_fee + ads_cost,
    }


def calculate_amazon_fee(sales_amount, referral_rate=0.15, fba_fee=0, ppc_cost=0):
    referral_fee = sales_amount * referral_rate
    return {
        "referral_fee": referral_fee,
        "fba_fee": fba_fee,
        "ppc_cost": ppc_cost,
        "total_fee": referral_fee + fba_fee + ppc_cost,
    }


def calculate_shopee_fee(sales_amount, transaction_rate=0.02, service_rate=0, ads_cost=0):
    transaction_fee = sales_amount * transaction_rate
    service_fee = sales_amount * service_rate
    return {
        "transaction_fee": transaction_fee,
        "service_fee": service_fee,
        "ads_cost": ads_cost,
        "total_fee": transaction_fee + service_fee + ads_cost,
    }
