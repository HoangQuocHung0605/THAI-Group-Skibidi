import React, { useState, useEffect, useRef } from 'react';
import { chatAPI } from '../services/api';

function Chat() {
  // Danh sách tin nhắn, mỗi tin có dạng: { role: 'user'|'bot', content: '...', sources: [] }
  const [messages, setMessages] = useState([]);

  // Nội dung người dùng đang gõ
  const [input, setInput] = useState('');

  // Đang chờ phản hồi từ backend hay không
  const [loading, setLoading] = useState(false);

  // Dùng để tự động cuộn xuống tin nhắn mới nhất
  const bottomRef = useRef(null);

  // Mỗi khi messages thay đổi, cuộn xuống cuối
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Hàm gửi tin nhắn
  const handleSend = async () => {
    // Không gửi nếu input trống hoặc đang loading
    if (!input.trim() || loading) return;

    // Thêm tin nhắn của user vào danh sách
    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);

    // Xóa input và bắt đầu loading
    setInput('');
    setLoading(true);

    try {
      // Gọi API backend
      const response = await chatAPI.sendMessage(input);

      // Lấy answer và sources từ response
      // Thử cả .answer và .message phòng backend đặt tên khác
      const answer = response.data?.answer
        || response.data?.message
        || 'Không có phản hồi từ server';
      const sources = response.data?.sources || [];

      // Thêm tin nhắn bot vào danh sách
      const botMessage = { role: 'bot', content: answer, sources };
      setMessages(prev => [...prev, botMessage]);

    } catch (error) {
      // Nếu lỗi thì hiện thông báo lỗi thay vì crash app
      const errorMessage = {
        role: 'bot',
        content: 'Lỗi kết nối backend. Vui lòng kiểm tra lại server.',
        sources: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      // Dù thành công hay lỗi đều tắt loading
      setLoading(false);
    }
  };

  // Bấm Enter để gửi, Shift+Enter để xuống dòng
  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  // Khi bấm vào câu hỏi gợi ý thì điền vào input
  const handleSuggestion = (question) => {
    setInput(question);
  };

  return (
    <div className="chat-container">

      {/* ===== HEADER ===== */}
      <div className="chat-header">
        <h2>Hỏi đáp về GitLab Handbook</h2>
        <p>Đặt câu hỏi về nội dung Handbook GitLab</p>
      </div>

      {/* ===== KHU VỰC TIN NHẮN ===== */}
      <div className="chat-messages">

        {/* Hiện gợi ý khi chưa có tin nhắn nào */}
        {messages.length === 0 && (
          <div className="chat-empty">
            <h1>SKIBIDI CHAT</h1>
            <p>Xin chào! Hãy đặt câu hỏi về GitLab Handbook</p>

            {/* Các câu hỏi gợi ý */}
            <div className="suggestions">
              {[
                'GitLab values la gi?',
                'Quy trinh onboarding?',
                'Remote work policy?'
              ].map(question => (
                <button
                  key={question}
                  className="suggestion-btn"
                  onClick={() => handleSuggestion(question)}
                >
                  {question}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Render từng tin nhắn */}
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.role}`}>

            {/* Avatar user hoặc bot */}
            <div className="message-avatar">
              {/* icon user hoặc bot */}
            </div>

            <div className="message-body">
              {/* Nội dung tin nhắn */}
              <div className="message-content">
                {message.content}
              </div>

              {/* Hiện sources nếu có */}
              {message.sources && message.sources.length > 0 && (
                <div className="message-sources">
                  <span>Nguon tham khao:</span>
                  {message.sources.map((source, i) => (
                    <a
                      key={i}
                      href={source}
                      target="_blank"
                      rel="noreferrer"
                      className="source-link"
                    >
                      {source}
                    </a>
                  ))}
                </div>
              )}
            </div>

          </div>
        ))}

        {/* Hiện loading khi đang chờ bot trả lời */}
        {loading && (
          <div className="message bot">
            <div className="message-avatar">
              {/* icon bot */}
            </div>
            <div className="message-body">
              {/* 3 chấm nhảy */}
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}

        {/* Điểm neo để cuộn xuống cuối */}
        <div ref={bottomRef} />

      </div>

      {/* ===== KHU VỰC NHẬP TIN NHẮN ===== */}
      <div className="chat-input-area">

        <textarea
          className="chat-input"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Nhập câu hỏi... (Enter để gửi, Shift+Enter xuống dòng)"
          rows={1}
          disabled={loading}
        />

        <button
          className="send-btn"
          onClick={handleSend}
          // Disable khi đang loading hoặc input trống
          disabled={loading || !input.trim()}
        >
           <span style={{ fontSize: '32px', lineHeight: 1 }}>⬆</span>
        </button>

      </div>

    </div>
  );
}

export default Chat;