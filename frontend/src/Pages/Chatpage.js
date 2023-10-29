import { Box, Divider } from "@chakra-ui/layout";
import { useState } from "react";
import { ChatState } from "../Context/ChatProvider";
import Header from "../components/basecomponents/Header";
import Chat from "../components/basecomponents/Chat";

const Chatpage = () => {
  const [fetchAgain, setFetchAgain] = useState(false);
  const { user } = ChatState();

  return (
    <div className="w-100">
      <Header />
      <Chat />
    </div>
  );
};

export default Chatpage;
