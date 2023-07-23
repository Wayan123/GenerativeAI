import sendBtnIcon from "../images/send-btn-icon.png";

export const ChatInput = function ({ searchText, setSearchText, setInput }) {
  const handleInputChange = (e) => {
    setSearchText(e.target.value);
  };

  const handleSubmit = (e) => {
    setInput(searchText);
  };

  return (
    <div className="chatbot-input-container">
      <input
        name="user-input"
        value={searchText}
        placeholder="Enter your query here.."
        type="text"
        id="user-input"
        required
        onChange={handleInputChange}
      />
      <button id="submit-btn" className="submit-btn" onClick={handleSubmit}>
        <img src={sendBtnIcon} className="send-btn-icon" />
      </button>
    </div>
  );
};
