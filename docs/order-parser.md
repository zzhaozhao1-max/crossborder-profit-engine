# Order Parser Module

## Purpose

Normalize marketplace order exports into a common format.

## Supported Sources

- Amazon
- TikTok Shop
- Shopee
- Walmart

## Standard Fields

```json
{
  "order_id": "",
  "sku": "",
  "product_name": "",
  "amount": 0,
  "refund": 0,
  "currency": "USD"
}
```

## Pipeline

File Upload → Parser → Normalized Orders → Profit Engine → Dashboard

Future versions will add platform-specific column mapping and settlement matching.
