
// function App() {
//   return (
//     <div style={{ padding: "2rem" }}>
//       <h1>Sales AI Agent</h1>
//       <Upload />
//     </div>
//   );
// }

// export default App;

import { useState } from "react";
import SummaryCards from "./components/SummaryCards";
import Upload from "./components/Upload";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "40px" }}>
      <h2>Sales Overview</h2>

      {/* Upload CSV + trigger KPI calculation */}
      <Upload onMetricsLoaded={setSummary} />

      {/* Show KPIs only after data exists */}
      {summary && <SummaryCards data={summary} />}
    </div>
  );
}

export default App;