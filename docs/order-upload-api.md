# Order Upload API Design

## Endpoint

POST /api/orders/upload

## Supported files

- CSV
- XLSX

## Processing flow

1. Upload marketplace report
2. Detect file format
3. Normalize order fields
4. Match refunds
5. Generate profit analysis

## Planned output

- Total orders
- Valid orders
- Refund orders
- Revenue
- SKU ranking
- Profit ranking

## Target platforms

- Amazon
- TikTok Shop
- Shopee
- Walmart
