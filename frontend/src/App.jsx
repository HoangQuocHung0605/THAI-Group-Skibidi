import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    // TODO: Integrate with backend API
  };

  return (
    <div className="App">
      <h1>RAG Solution Chat</h1>
      {/* Chat UI - HIEC viet lai */}
    </div>
  );
}

export default App;
