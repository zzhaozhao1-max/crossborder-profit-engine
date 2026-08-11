export default function AnalyticsCards() {
  const cards = [
    { title: 'Revenue', value: '$0' },
    { title: 'Profit', value: '$0' },
    { title: 'Margin', value: '0%' },
    { title: 'ROI', value: '0' },
  ];

  return (
    <div className="grid grid-cols-2 gap-4">
      {cards.map((card) => (
        <div key={card.title} className="rounded-lg border p-4">
          <div className="text-sm text-gray-500">{card.title}</div>
          <div className="mt-2 text-2xl font-bold">{card.value}</div>
        </div>
      ))}
    </div>
  );
}
