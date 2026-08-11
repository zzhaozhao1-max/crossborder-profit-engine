# Backend

## V0.1 Profit Calculator API

Backend services will provide calculation APIs for cross-border sellers.

Planned modules:

```
backend/
 ├── app/
 │   ├── calculator/
 │   │   └── profit_engine.py
 │   ├── currency/
 │   │   └── exchange.py
 │   ├── marketplace/
 │   │   └── fees.py
 │   └── main.py
```

## Main calculation inputs

- Selling price
- Product cost
- Shipping cost
- Platform commission
- Advertising cost
- Refund rate
- Currency exchange rate

## Main outputs

- Net profit
- Profit margin
- ROI
- Break-even advertising cost
