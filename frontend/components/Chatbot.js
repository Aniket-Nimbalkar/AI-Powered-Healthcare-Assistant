import React, { useState } from "react";
import axios from "axios";
import "./Chatbot.css";

const Chatbot = () => {
  const [query, setQuery] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!query.trim()) return;
    setChat([...chat, { text: query, type: "user" }]);

    const response = await axios.post("http://127.0.0.1:5000/chat", { query });
    setChat([...chat, { text: query, type: "user" }, { text: response.data.response, type: "bot" }]);
    setQuery("");
  };

  return (
    <div className="chat-container">
      <h2>Medical Chatbot</h2>
      <div className="chat-box">
        {chat.map((msg, index) => (
          <div key={index} className={msg.type}>
            {msg.text}
          </div>
        ))}
      </div>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask me anything..." />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chatbot;
