import React from 'react';

export default function ReportDashboard() {
  return (
    <div className="report-dashboard">
      <h1>Profit Report</h1>
      <div className="metrics">
        <div>Revenue</div>
        <div>Cost</div>
        <div>Profit</div>
        <div>Margin</div>
      </div>
      <section>
        <h2>SKU Ranking</h2>
        <p>Top products by profit will appear here.</p>
      </section>
    </div>
  );
}
