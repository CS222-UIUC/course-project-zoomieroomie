import React, { useEffect } from "react";

interface Roommate {
  first: string;
  email: string;
}

const RoommateMatches: React.FC = () => {
  console.log("inside the script");
  const best_roommate: Roommate | null = null; // replace with your actual logic to find the best roommate

  useEffect(() => {
    const div = document.getElementById("match");
    if (best_roommate) {
      console.log("match found");
      const name_label = document.createElement("label");
      name_label.textContent = "Name: " + best_roommate;
      const email_label = document.createElement("label");
      email_label.textContent = "Email: " + best_roommate;
      if (div) {
        div.appendChild(name_label);
        div.appendChild(email_label);
      }
    } else {
      console.log("no match");
      const label = document.createElement("label");
      label.textContent = "No matches found.";
      if (div) {
        div.appendChild(label);
      }
    }
  }, [best_roommate]);

  return (
    <>
      <h1>Your Best Roommate:</h1>
      <div id="match"></div>
    </>
  );
};

export default RoommateMatches;
