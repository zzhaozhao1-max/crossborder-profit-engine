import React from "react";

export default function FeatureSection() {
  const features = [
    "Multi marketplace profit calculation",
    "Order and settlement matching",
    "AI business diagnosis",
    "Automated reports",
  ];

  return (
    <section className="grid gap-4 md:grid-cols-4">
      {features.map((item) => (
        <div key={item} className="rounded-lg bg-white p-5 shadow-sm">
          {item}
        </div>
      ))}
    </section>
  );
}
