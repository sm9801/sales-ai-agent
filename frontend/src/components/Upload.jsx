import { useState } from "react";
import api from "../api";
import { getSummaryMetrics } from "../api";

function Upload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await api.post("/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Upload failed");
    }
  };

  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>Upload Sales Data</h2>

      <input
        type="file"
        accept=".csv,.xlsx"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>Upload</button>

      {result && (
        <div>
            <p style={{ color: "green", fontWeight: "bold" }}>
            {result.message}
          </p>
          <p>Rows: {result.rows}</p>
          <p>Columns: {result.columns}</p>
          <p>Fields: {result.column_names.join(", ")}</p>
        </div>
      )}

      <button
        onClick={async () => {
        const data = await getSummaryMetrics();
        console.log("KPIs:", data);
    }}
    style={{ marginTop: "1rem" }}
>
  Test KPI Endpoint
</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}

export default Upload;

