import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import AirportManagement from "./components/AirportManagement";

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/manage" element={<AirportManagement />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
