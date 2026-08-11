export default function ProfitOverview({data}: {data:any}) {
  return (
    <div>
      <h2>Profit Overview</h2>
      <div>Revenue: {data?.revenue ?? 0}</div>
      <div>Profit: {data?.profit ?? 0}</div>
      <div>Margin: {data?.margin ?? 0}</div>
    </div>
  );
}
