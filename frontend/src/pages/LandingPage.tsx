import React from "react";

export default function LandingPage() {
  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <section className="mx-auto max-w-6xl px-6 py-20">
        <h1 className="text-5xl font-bold">CrossBorder Profit Engine</h1>
        <p className="mt-6 max-w-2xl text-lg text-slate-600">
          AI-powered profit analytics platform for Amazon, TikTok Shop, Shopee and Walmart sellers.
        </p>
        <div className="mt-10 grid gap-6 md:grid-cols-4">
          {[
            ["Revenue", "Track sales"],
            ["Profit", "Calculate real margin"],
            ["ROI", "Analyze ads"],
            ["AI Insights", "Find optimization opportunities"],
          ].map(([title, text]) => (
            <div className="rounded-xl bg-white p-6 shadow" key={title}>
              <h3 className="font-semibold">{title}</h3>
              <p className="mt-2 text-sm text-slate-500">{text}</p>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
