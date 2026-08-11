export default function PlatformLogos() {
  const platforms = ["Amazon", "TikTok Shop", "Shopee", "Walmart", "Shopify"];

  return (
    <section className="platform-logos">
      {platforms.map((platform) => (
        <div key={platform}>{platform}</div>
      ))}
    </section>
  );
}
