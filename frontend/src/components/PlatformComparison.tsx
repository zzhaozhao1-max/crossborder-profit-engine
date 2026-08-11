export default function PlatformComparison(){
 const platforms=['Amazon','TikTok Shop','Shopee','Walmart'];
 return <div>{platforms.map(p=><div key={p}>{p}: $0</div>)}</div>;
}
