export interface ProfitRequest {
  selling_price: number;
  product_cost: number;
  shipping_cost: number;
  platform_fee: number;
  advertising_cost: number;
}

export interface ProfitResponse {
  revenue: number;
  total_cost: number;
  profit: number;
  profit_margin: number;
}

const API_BASE_URL = "http://localhost:8000";

export async function calculateProfit(
  data: ProfitRequest
): Promise<ProfitResponse> {
  const response = await fetch(`${API_BASE_URL}/api/profit/calculate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Profit calculation failed");
  }

  return response.json();
}
