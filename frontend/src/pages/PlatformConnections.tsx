export default function PlatformConnections(){
  const platforms=['Amazon','TikTok Shop','Shopee','Walmart'];
  return <div><h1>Platform Connections</h1>{platforms.map(p=><div key={p}>{p}<button>Connect</button></div>)}</div>
}
