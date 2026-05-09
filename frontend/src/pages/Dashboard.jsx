import React, { useState, useEffect } from 'react';
import { ingestAPI } from '../services/api';

function Dashboard() {
  // Trạng thái hệ thống lấy từ backend (số tài liệu, số vectors...)
  const [status, setStatus] = useState(null);

  // Đang tải trạng thái hệ thống hay không
  const [statusLoading, setStatusLoading] = useState(true);

  // Lỗi khi lấy trạng thái
  const [statusError, setStatusError] = useState('');

  // File đang được chọn để upload
  const [selectedFile, setSelectedFile] = useState(null);

  // Đang upload hay không
  const [uploading, setUploading] = useState(false);

  // Thông báo sau khi upload (thành công hoặc thất bại)
  const [uploadMessage, setUploadMessage] = useState('');

  // Khi component load lần đầu, lấy trạng thái hệ thống từ backend
  useEffect(() => {
    fetchStatus();
  }, []);

  // Hàm gọi API lấy trạng thái hệ thống
  const fetchStatus = async () => {
    setStatusLoading(true);
    setStatusError('');
    try {
      const response = await ingestAPI.getStatus();
      setStatus(response.data);
    } catch (error) {
      setStatusError('Khong the ket noi backend. Kiem tra lai server.');
    } finally {
      setStatusLoading(false);
    }
  };

  // Khi người dùng chọn file từ input
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // Chỉ cho phép file PDF hoặc TXT
    const allowedTypes = ['application/pdf', 'text/plain'];
    if (!allowedTypes.includes(file.type)) {
      setUploadMessage('Chi ho tro file PDF hoac TXT.');
      return;
    }

    // Giới hạn 10MB
    const maxSize = 10 * 1024 * 1024;
    if (file.size > maxSize) {
      setUploadMessage('File qua lon. Toi da 10MB.');
      return;
    }

    // File hợp lệ thì lưu vào state
    setSelectedFile(file);
    setUploadMessage('');
  };

  // Hàm gửi file lên backend
  const handleUpload = async () => {
    // Không làm gì nếu chưa chọn file hoặc đang upload
    if (!selectedFile || uploading) return;

    setUploading(true);
    setUploadMessage('');

    try {
      await ingestAPI.uploadDocument(selectedFile);

      setUploadMessage('Upload Thành công!');

      // Reset file đã chọn sau khi upload xong
      setSelectedFile(null);

      // Cập nhật lại trạng thái hệ thống vì vừa thêm tài liệu mới
      fetchStatus();

    } catch (error) {
      setUploadMessage('Upload thất bại. Vui lòng thử lại.');
    } finally {
      setUploading(false);
    }
  };

  // Hàm format kích thước file cho dễ đọc
  // Ví dụ: 1024 → "1.00 KB", 1048576 → "1.00 MB"
  const formatFileSize = (bytes) => {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(2)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
  };

  return (
    <div className="dashboard-container">

      {/* ===== HEADER ===== */}
      <div className="dashboard-header">
        <h2>Dashboard</h2>
        <p>Quản lí tài liệu và theo dõi trạng thái hệ thống</p>
      </div>

      <div className="dashboard-grid">

        {/* ===== CARD 1: UPLOAD TÀI LIỆU ===== */}
        <div className="card">
          <h3>Upload Tài Liệu</h3>
          <p>Thêm tài liệu mới vào hệ thống RAG</p>

          {/* Khu vực chọn file */}
          <div className="upload-area">

            {/* Input file ẩn, được trigger bởi label bên dưới */}
            <input
              id="file-input"
              type="file"
              hidden
              accept=".pdf,.txt"
              onChange={handleFileChange}
              disabled={uploading}
            />

            {/* Bấm vào đây để mở hộp thoại chọn file */}
            <label htmlFor="file-input" className="file-label">
              Chọn file (PDF Hoặc TXT, tối đa 10MB)
            </label>

            {/* Hiện tên và kích thước file đã chọn */}
            {selectedFile && (
              <div className="file-info">
                <span className="file-name">{selectedFile.name}</span>
                <span className="file-size">{formatFileSize(selectedFile.size)}</span>
              </div>
            )}

            {/* Nút upload, chỉ hiện khi đã chọn file */}
            {selectedFile && (
              <button
                className="upload-btn"
                onClick={handleUpload}
                disabled={uploading}
              >
                {/* Đổi text khi đang upload */}
                {uploading ? 'Đang upload...' : 'Upload'}
              </button>
            )}

          </div>

          {/* Thông báo kết quả upload */}
          {uploadMessage && (
            <p className={`upload-message ${uploadMessage.includes('thành công') ? 'success' : 'error'}`}>
              {uploadMessage}
            </p>
          )}
        </div>

        {/* ===== CARD 2: TRẠNG THÁI HỆ THỐNG ===== */}
        <div className="card">
          <div className="card-title-row">
            <h3>Trạng Thái Hệ Thống</h3>

            {/* Nút refresh để lấy lại trạng thái mới nhất */}
            <button
              className="refresh-btn"
              onClick={fetchStatus}
              disabled={statusLoading}
            >
              {statusLoading ? 'Đang tải...' : 'Làm mới'}
            </button>
          </div>

          {/* Đang tải */}
          {statusLoading && (
            <p className="status-loading">Đang tải trạng thái...</p>
          )}

          {/* Lỗi khi tải */}
          {statusError && !statusLoading && (
            <p className="status-error">{statusError}</p>
          )}

          {/* Hiện thông tin trạng thái khi tải xong */}
          {status && !statusLoading && (
            <div className="status-info">

              {/* Số tài liệu đã ingest */}
              <div className="status-row">
                <span className="status-label">Tài liệu:</span>
                <span className="status-value">
                  {/* Thử cả total_documents và document_count phòng backend đặt tên khác */}
                  {status.total_documents ?? status.document_count ?? 'N/A'}
                </span>
              </div>

              {/* Số vectors trong Qdrant */}
              <div className="status-row">
                <span className="status-label">Vectors:</span>
                <span className="status-value">
                  {status.total_vectors ?? status.vector_count ?? 'N/A'}
                </span>
              </div>

              {/* Trạng thái hoạt động */}
              <div className="status-row">
                <span className="status-label">Trạng thái:</span>
                <span className={`status-value ${status.status === 'active' ? 'active' : ''}`}>
                  {status.status ?? 'N/A'}
                </span>
              </div>

            </div>
          )}
        </div>

      </div>
    </div>
  );
}

export default Dashboard;