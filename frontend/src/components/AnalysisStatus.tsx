export default function AnalysisStatus({status}:{status:string}) {
  return (
    <div className="analysis-status">
      <h3>Analysis Status</h3>
      <p>{status}</p>
    </div>
  )
}
