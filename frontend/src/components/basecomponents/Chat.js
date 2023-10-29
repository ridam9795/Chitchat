import React from "react";
import ChatList from "./ChatList";
import ChatBox from "./ChatBox";

export default function Chat() {
  return (
    <div>
      <div className="row">
        <div className="col-3">
          <ChatList />
        </div>
        <div className="col-9">
          <ChatBox />
        </div>
      </div>
    </div>
  );
}
