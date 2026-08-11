# Database Models

## Seller
- id
- name
- default_currency

## Product / SKU
- id
- sku
- product_name
- cost
- shipping_cost

## Order
- id
- order_number
- platform
- order_date
- revenue
- refund_amount

## Profit Record
- id
- sku_id
- revenue
- total_cost
- profit
- margin

Planned database: PostgreSQL + SQLAlchemy.
