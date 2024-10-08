import React from "react";
import PropTypes from "prop-types";
import Message from "./Message";

function MessageList({
  messages,
  currentUser,
  onMessageDelete,
  onUpdateMessage,
}) {
  return (
    <div className="list">
      <ul>
        {messages.map((message) => (
          <Message
            key={message.id}
            message={message}
            currentUser={currentUser}
            onMessageDelete={onMessageDelete}
            onUpdateMessage={onUpdateMessage}
          />
        ))}
      </ul>
    </div>
  );
}


MessageList.propTypes = {
  messages: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      text: PropTypes.string.isRequired,
      user_id: PropTypes.number.isRequired,
      created_at: PropTypes.string.isRequired,
    })
  ).isRequired,
  currentUser: PropTypes.shape({
    username: PropTypes.string.isRequired,
  }).isRequired,
  onMessageDelete: PropTypes.func.isRequired,
  onUpdateMessage: PropTypes.func.isRequired,
};

export default MessageList;
