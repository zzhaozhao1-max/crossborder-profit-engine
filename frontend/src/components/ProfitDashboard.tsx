import React from "react";

export default function ProfitDashboard() {
  const metrics = [
    { title: "Revenue", value: "$0" },
    { title: "Profit", value: "$0" },
    { title: "Margin", value: "0%" },
    { title: "ROI", value: "0" },
  ];

  return (
    <div>
      <h1>CrossBorder Profit Engine</h1>
      <p>Cross-border e-commerce profitability dashboard.</p>
      <div>
        {metrics.map((item) => (
          <div key={item.title}>
            <h3>{item.title}</h3>
            <p>{item.value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
