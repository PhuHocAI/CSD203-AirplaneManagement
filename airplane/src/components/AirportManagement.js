import React from "react";

function AirportManagement() {
  const styles = {
    box: {
      border: "1px solid blue",
      margin: "10px",
      padding: "10px",
      cursor: "pointer",
    },
    container: { display: "flex", flexDirection: "column" },
  };

  return (
    <div style={styles.container}>
      <div style={styles.box} onClick={() => alert("Add an Airport")}>
        Add an Airport
      </div>
      <div style={styles.box} onClick={() => alert("Delete an Airport")}>
        Delete an Airport
      </div>
      <div
        style={styles.box}
        onClick={() => alert("Update Airport Information")}
      >
        Update Airport Information
      </div>
      <div style={styles.box} onClick={() => alert("Display Airport System")}>
        Display Airport System
      </div>
      <div style={styles.box} onClick={() => alert("Calculate Cost")}>
        Calculate Cost (Time, Cost)
      </div>
      <div style={styles.box} onClick={() => alert("Find the Shortest Route")}>
        Find the Shortest Route
      </div>
    </div>
  );
}

export default AirportManagement;
