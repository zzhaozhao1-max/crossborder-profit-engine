import ProfitCalculator from './ProfitCalculator';
import CurrencyConverter from './CurrencyConverter';
import OrderAnalytics from './OrderAnalytics';

export default function Dashboard() {
  return (
    <main>
      <h1>CrossBorder Profit Engine</h1>
      <p>Analytics dashboard for global e-commerce sellers.</p>
      <section>
        <ProfitCalculator />
        <CurrencyConverter />
        <OrderAnalytics />
      </section>
    </main>
  );
}
