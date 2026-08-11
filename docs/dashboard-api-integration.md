# Dashboard API Integration

## Data Flow

Frontend Dashboard -> API Service -> FastAPI Backend -> Analytics Engine

## Dashboard Metrics

- Revenue
- Total Cost
- Net Profit
- Profit Margin
- ROI
- Top Performing SKU

## Future API Endpoints

`GET /api/dashboard/summary`

Returns aggregated business metrics.

`GET /api/dashboard/products`

Returns SKU profitability ranking.

`POST /api/dashboard/upload`

Accepts CSV/XLSX order files for analysis.
