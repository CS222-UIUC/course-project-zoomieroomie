import React from "react";
import "../css/Main.css"; // Import the Main.css file

const Main = () => {
  return (
    <div className="main-container">
      <h1 className="welcome-heading">Welcome!</h1>
      <div className="buttons-container">
        <button className="button" onClick={() => alert("View Your Matches clicked")}>View Your Matches</button>
        <button className="button" onClick={() => alert("Create Your Profile clicked")}>Create Your Profile</button>
        <button className="button" onClick={() => alert("Sign Out clicked")}>Sign Out</button>
      </div>
    </div>
  );
};

export default Main;