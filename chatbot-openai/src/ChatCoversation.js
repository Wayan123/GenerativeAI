export const ChatCoversation = function ({ conversationArr }) {
  return (
    <div className="chatbot-conversation-container" id="chatbot-conversation">
      {conversationArr.map((item, index) => (
        <div
          className={`speech ${
            item.role === "user" ? "speech-user" : "speech-assistant"
          }`}
          key={index}
        >
          <div className="speech-username">{item.role}</div>
          <div className="speech-content">{item.content}</div>
        </div>
      ))}
    </div>
  );
};
