import owlLogo from "../images/owl-logo.png";

const Header = () => {
  return (
    <div className="chatbot-header">
      <img src={owlLogo} className="logo" />
      <h1>GetItAll</h1>
      <h2>Ask me anything!</h2>
      <p className="supportId">User ID: 1234</p>
    </div>
  );
};

export default Header;
