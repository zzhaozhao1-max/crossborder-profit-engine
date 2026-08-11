import React, { useState } from 'react';

export default function ProfitCalculator() {
  const [price, setPrice] = useState(0);
  const [cost, setCost] = useState(0);
  const [shipping, setShipping] = useState(0);
  const [fees, setFees] = useState(0);
  const [ads, setAds] = useState(0);

  const profit = price - cost - shipping - fees - ads;
  const margin = price ? (profit / price) * 100 : 0;

  return (
    <div>
      <h2>Profit Calculator</h2>
      <input placeholder="Selling Price" onChange={e => setPrice(Number(e.target.value))} />
      <input placeholder="Product Cost" onChange={e => setCost(Number(e.target.value))} />
      <input placeholder="Shipping Cost" onChange={e => setShipping(Number(e.target.value))} />
      <input placeholder="Platform Fees" onChange={e => setFees(Number(e.target.value))} />
      <input placeholder="Advertising Cost" onChange={e => setAds(Number(e.target.value))} />
      <p>Profit: {profit.toFixed(2)}</p>
      <p>Margin: {margin.toFixed(2)}%</p>
    </div>
  );
}
