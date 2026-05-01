import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Chat API
export const chatAPI = {
  sendMessage: (message) => apiClient.post('/chat', { message }),
  getHistory: () => apiClient.get('/chat/history'),
};

// Ingest API
export const ingestAPI = {
  uploadDocument: (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/ingest', formData);
  },
  getStatus: () => apiClient.get('/ingest/status'),
};
