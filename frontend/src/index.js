import React from "react";
import "./index.css";
import App from "./App";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter as Router } from "react-router-dom";
import ChatProvider from "../src/Context/ChatProvider";
import { createRoot } from "react-dom/client";
import 'jquery/dist/jquery.min.js';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
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
