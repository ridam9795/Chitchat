import "./App.css";
import Homepage from "./Pages/Homepage";
import { Routes, Route } from "react-router-dom";
import Chatpage from "./Pages/Chatpage";
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Homepage />} exact></Route>

        <Route path="/chats" element={<Chatpage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
