import React, { useEffect, useState } from "react";
import NewMessage from "./NewMessage";
import MessageList from "./MessageList";

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/messages")
      .then((r) => {
        if (r.ok) return r.json();
        throw r;
      })
      .then((data) => setMessages(data))
      .catch((err) => console.log("Error fetching messages:", err));
  }, []);

  function handleAddMessage(newMessage) {
    setMessages([...messages, newMessage]);
  }

  return (
    <div>
      <h1>Chatterbox</h1>
      <NewMessage onAddMessage={handleAddMessage} />
      <MessageList messages={messages} />
    </div>
  );
}

export default App;
