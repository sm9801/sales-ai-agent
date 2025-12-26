import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const pingBackend = async () => {
  const res = await api.get("/ping");
  return res.data;
};

// export const getSummaryMetrics = async () => {
//   const res = await api.get("/metrics/summary");
//   return res.data;
// };
export const uploadCSV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await api.post("/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return res.data;
};

export const fetchSummaryMetrics = async () => {
  const res = await api.get(`/metrics/summary`);
  return res.data;
};

export async function fetchTimeMetrics() {
  const res = await api.get(`/metrics/time`);
  return res.json();
}

export async function fetchProductMetrics() {
  const res = await api.get(`/metrics/product`);
  return res.json();
}

export async function fetchBrandMetrics() {
  const res = await api.get(`/metrics/brand`);
  return res.json();
}

export async function fetchPlatformMetrics() {
  const res = await api.get(`/metrics/platform`);
  return res.json();
}

export default api;

