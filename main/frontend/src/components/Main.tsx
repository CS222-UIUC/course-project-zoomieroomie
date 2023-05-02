import React from "react";
import "../css/Main.css"; // Import the Main.css file
import { Link } from "react-router-dom";

const Main: React.FC = () => {
  return (
    <div className="main-container">
      <h1 className="welcome-heading">Welcome to Zoomie Roomie!</h1>
      <div className="buttons-container">
        <button type="submit">
         
          <Link to="/matches">View Your Matches</Link>
        </button>
        <button type="submit">
          
          <Link to="/preferencesform">Fill out the Preferences Form</Link>
        </button>
        <button type="submit">
        
          <Link to="/login">Sign Out</Link>
        </button>
      </div>
    </div>
  );
};

export default Main;
