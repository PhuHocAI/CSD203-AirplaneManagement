import React from "react";
import logo from "../assets/depositphotos_705817886-stock-illustration-commercial-aeroplane-icon-vector-illustration.jpg";
function Home() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh", // Thiết lập chiều cao view-port để nội dung có thể giữa khung theo chiều dọc
        color: "blue",
      }}
    >
      <img src={logo} alt="Logo" style={{ width: "150px" }} />{" "}
      {/* Điều chỉnh kích thước logo theo nhu cầu */}
      <h1>Welcome to Airport Management System</h1>
      <p>This is a system to manage different aspects of airports.</p>
    </div>
  );
}

export default Home;
