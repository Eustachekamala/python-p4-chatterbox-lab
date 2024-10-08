import React, { useState } from "react";

function EditMessage({ id, body, onUpdateMessage }) {
  const [messageBody, setMessageBody] = useState(body);

  async function handleFormSubmit(e) {
    e.preventDefault();

    try {
      const response = await fetch(`http://127.0.0.1:5555/messages/${id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: messageBody,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to update message");
      }

      const updatedMessage = await response.json();
      onUpdateMessage(updatedMessage);
    } catch (error) {
      console.error("Error updating message:", error);
    }
  }

  return (
    <form className="edit-message" onSubmit={handleFormSubmit}>
      <input
        type="text"
        name="body"
        autoComplete="off"
        value={messageBody}
        onChange={(e) => setMessageBody(e.target.value)}
      />
      <input type="submit" value="Save" />
    </form>
  );
}

export default EditMessage;
