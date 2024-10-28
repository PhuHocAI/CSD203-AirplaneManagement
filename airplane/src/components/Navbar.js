import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/depositphotos_705817886-stock-illustration-commercial-aeroplane-icon-vector-illustration.jpg";
import "./Navbar.css";

function Navbar() {
  return (
    <div className="navbar">
      <img src={logo} alt="Airplane Logo" className="navbar-logo" />
      <div className="navbar-links">
        <Link to="/" className="nav-link">
          Home
        </Link>
        <Link to="/manage" className="nav-link">
          Manage
        </Link>
      </div>
      <div className="navbar-auth">
        <Link to="/login" className="nav-link">
          Log in
        </Link>
        <Link to="/register" className="nav-link">
          Register
        </Link>
      </div>
    </div>
  );
}

export default Navbar;
