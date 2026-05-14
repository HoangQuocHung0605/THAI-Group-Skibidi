import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import Chat from './pages/Chat';
import Dashboard from './pages/Dashboard';
import './App.css';

function App() {
  // State lưu chế độ sáng/tối, mặc định là tối
  const [darkMode, setDarkMode] = useState(true);
  return (
    <Router>
      <div className={darkMode ? 'app dark' : 'app light'}>

        <nav className="navbar">
          <div className="navbar-brand">
            <span className="brand-icon">🦊</span>
            <span className="brand-name">GitLab Handbook QA</span>
          </div>
          <div className="navbar-links">
            <NavLink
              to="/"
              end
              className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
            >
              Chat
            </NavLink>
            <NavLink
              to="/dashboard"
              className={({ isActive }) => isActive ? 'nav-link active' : 'nav-link'}
            >
              Dashboard
            </NavLink>
          </div>
        </nav>

        <div className="content-wrapper">

    {/* ===== SIDEBAR ===== */}
    <aside className="sidebar">

      {/* Nút tạo đoạn chat mới */}
      <button className="new-chat-btn">
        ✏️ Đoạn chat mới
      </button>
      

      {/* Thanh tìm kiếm */}
      <div className="search-box">
        <span className="search-icon">🔍</span>
        <input
          type="text"
          placeholder="Tìm kiếm đoạn chat"
          className="search-input"
        />
      </div>

    
    {/* Nút chuyển chế độ sáng/tối — đẩy xuống cuối sidebar */}
  <div className="theme-toggle" onClick={() => setDarkMode(!darkMode)}>
    <span>{darkMode ? '☀️' : '🌙'}</span>
    <span>{darkMode ? 'Chế độ sáng' : 'Chế độ tối'}</span>
  </div>

</aside>

    {/* ===== NỘI DUNG CHÍNH ===== */}
    <main className="main-content">
      <Routes>
        <Route path="/" element={<Chat />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </main>

</div>

      </div>
    </Router>
  );
}

export default App;