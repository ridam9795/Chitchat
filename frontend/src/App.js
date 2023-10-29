import "./App.css";
import Homepage from "./Pages/Homepage";
import { Routes, Route } from "react-router-dom";
import Chatpage from "./Pages/Chatpage";
import VerifyOTP from "./components/authentication/VerifyOTP";
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Homepage />} exact></Route>

        <Route path="/chats" element={<Chatpage />}></Route>
        <Route path="/verify_otp" element={<VerifyOTP />} />
      </Routes>
    </div>
  );
}

export default App;
