import React from "react";
import logo from "../assets/depositphotos_705817886-stock-illustration-commercial-aeroplane-icon-vector-illustration.jpg";
import "./Home.css";
function Home() {
  return (
    <div className="home-container">
      <img src={logo} alt="Airplane Logo" className="airplane-logo" />
      <h2 className="welcome-text">Welcome To The Airport Management System</h2>
      <p className="welcome-text text-content">
        This is a web application that allows you to manage your airport.
      </p>
    </div>
  );
}

export default Home;
