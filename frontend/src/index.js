import React from "react";
import "./index.css";
import App from "./App";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter as Router } from "react-router-dom";
import ChatProvider from "../src/Context/ChatProvider";
import { createRoot } from "react-dom/client";
const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <Router>
    <ChatProvider>
      <ChakraProvider>
        <App />
      </ChakraProvider>
    </ChatProvider>
  </Router>
);

// ReactDOM.render(
//   <ChatProvider>
//     <BrowserRouter>
//     <ChakraProvider>
//     <App />
//     </ChakraProvider>
//         </BrowserRouter>

//   </ChatProvider>,
//   document.getElementById('root')
// );
