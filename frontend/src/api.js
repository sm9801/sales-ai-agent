import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const pingBackend = async () => {
  const res = await api.get("/ping");
  return res.data;
};

export const getSummaryMetrics = async () => {
  const res = await api.get("/metrics/summary");
  return res.data;
};

export default api;

