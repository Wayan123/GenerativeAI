import Header from "./Header";
import { ChatCoversation } from "./ChatCoversation";
import { ChatInput } from "./ChatInput";
import { Configuration, OpenAIApi } from "openai";
import "./App.css";
import { useState, useEffect } from "react";
import * as keys from "./env.js";

//Open API Configuration
const configuration = new Configuration({
  apiKey: keys.API_KEY,
});

//Open API
const openai = new OpenAIApi(configuration);

function App() {
  const [searchText, setSearchText] = useState("");
  const [input, setInput] = useState("");
  const [conversationArr, setConversationArr] = useState([
    {
      role: "system",
      content: "You are a useful assitant",
    },
  ]);

  //When Submit Button is clicked
  useEffect(() => {
    if (input) {
      setSearchText("");
      //console.log(input);
      const newRequest = [
        ...conversationArr,
        {
          role: "user",
          content: input,
        },
      ];
      setConversationArr(newRequest);
      fetchReply(newRequest, setConversationArr);
    }
    return () => {
      console.log("cleanup...");
    };
  }, [input]);

  //Only while Page Loading..
  useEffect(() => {
    fetchReply(conversationArr, setConversationArr);
  }, []);

  // Scroll down automatically after a new message is added
  useEffect(() => {
    const conversationContainer = document.getElementById(
      "chatbot-conversation"
    );
    conversationContainer.scrollTop = conversationContainer.scrollHeight;
  }, [conversationArr]);

  return (
    <div className="chatbot-container">
      <Header />
      <ChatCoversation conversationArr={conversationArr} />
      <ChatInput
        searchText={searchText}
        setSearchText={setSearchText}
        setInput={setInput}
      />
    </div>
  );
}

//https://api.openai.com/v1/chat/completions
async function fetchReply(newRequest, setConversationArr) {
  const response = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: newRequest,
  });

  const newMessage = response?.data?.choices[0]?.message;

  //Add API Response to Array
  if (newMessage) {
    setConversationArr((prevArr) => [...prevArr, newMessage]);
  }
}

export default App;
