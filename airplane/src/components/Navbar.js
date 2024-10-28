import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/depositphotos_705817886-stock-illustration-commercial-aeroplane-icon-vector-illustration.jpg";
import "./Navbar.css";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-title">
        <img src={logo} alt="Airplane Logo" className="navbar-logo" />
      </div>

      <div className="navbar-links">
        <Link to="/" className="nav-link">
          Home
        </Link>
        <Link to="/manage" className="nav-link">
          Airport Management
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
