import React, { useState } from "react";
import EditMessage from "./EditMessage";

function Message({ message, currentUser, onMessageDelete, onUpdateMessage }) {
  const [isEditing, setIsEditing] = useState(false);

  const { id, username, text: body, created_at: createdAt } = message;
  const timestamp = new Date(createdAt).toLocaleTimeString();
  const isCurrentUser = currentUser.username === username;

  async function handleDeleteClick() {
    try {
      const response = await fetch(`http://127.0.0.1:5555/messages/${id}`, {
        method: "DELETE",
      });
      if (!response.ok) {
        throw new Error("Failed to delete message");
      }
      onMessageDelete(id);
    } catch (error) {
      console.error("Error deleting message:", error);
    }
  }

  function handleUpdateMessage(updatedMessage) {
    setIsEditing(false);
    onUpdateMessage(updatedMessage);
  }

  return (
    <li>
      <span className="user">{username}</span>
      <span className="time">{timestamp}</span>
      {isEditing ? (
        <EditMessage
          id={id}
          body={body}
          onUpdateMessage={handleUpdateMessage}
        />
      ) : (
        <p>{body}</p>
      )}
      {isCurrentUser && (
        <div className="actions">
          <button onClick={() => setIsEditing((prev) => !prev)}>
            <span role="img" aria-label="edit">
              ✏️
            </span>
          </button>
          <button onClick={handleDeleteClick}>
            <span role="img" aria-label="delete">
              🗑
            </span>
          </button>
        </div>
      )}
    </li>
  );
}

export default Message;
