export default function ExecutiveDashboard(){
  const cards=[
    {name:'Revenue',value:'$0'},
    {name:'Profit',value:'$0'},
    {name:'Orders',value:'0'},
    {name:'ROI',value:'0'}
  ];
  return <div>{cards.map(c=><div key={c.name}><h3>{c.name}</h3><p>{c.value}</p></div>)}</div>;
}
