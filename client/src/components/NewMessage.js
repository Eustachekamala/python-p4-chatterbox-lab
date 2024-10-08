import React, { useState } from "react";

function NewMessage({ currentUser, onAddMessage }) {
  const [text, setText] = useState(""); // Renamed for clarity
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5555/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text, // Using the updated state variable
          user_id: currentUser.id,
        }),
      });
  if (!response.ok) {
  const errorData = await response.json();
  console.error("Server Error:", errorData);
  throw new Error(errorData.message || "Failed to send message");
}

      const newMessage = await response.json();
      onAddMessage(newMessage);
      setText("");
    } catch (error) {
      console.error("Error sending message:", error);
      setError("Failed to send message. Please try again.");
    }
  }

  return (
    <form className="new-message" onSubmit={handleSubmit}>
      <input
        type="text"
        name="text" // Changed to match the JSON structure
        autoComplete="off"
        value={text}
        onChange={(e) => setText(e.target.value)}
        required
      />
      <button type="submit">Send</button>
      {error && <p className="error">{error}</p>}
    </form>
  );
}

export default NewMessage;
