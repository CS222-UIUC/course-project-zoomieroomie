import React, { useState } from "react";
import HabitsAndPreferences from "./preferences_form";

interface FormData {
  // Define the type of each form field
  smoke: string;
  "l-smoke": string;
  "l-drink": string;
  drink: string;
  extrovert: string;
  "l-extrovert": string;
  study: string;
  sleep: string;
  "bedtime-school": string;
  "bedtime-weekend": string;
  messy: string;
  "l-messy": string;
}

const MyForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    smoke: "",
    "l-smoke": "",
    "l-drink": "",
    drink: "",
    extrovert: "",
    "l-extrovert": "",
    study: "",
    sleep: "",
    "bedtime-school": "",
    "bedtime-weekend": "",
    messy: "",
    "l-messy": "",
  });

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const form = event.currentTarget;
    const formData = new FormData(form);

    let count = 0;
    let data: { [key: string]: any } = {};
    for (const entry of formData.entries()) {
      const name = entry[0];
      const value = entry[1];
      count += 1;
      data[name] = value;
}

    if (count !== 12) {
      alert("PLEASE SELECT A RESPONSE FOR ALL QUESTIONS.");
    } else {
      try {
        const proxyUrl = "https://cors-anywhere.herokuapp.com/";
        const apiUrl = "http://127.0.0.1:5000/submit-form";
        const response = await fetch(proxyUrl + apiUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ data }),
        });
        alert("Form submitted successfully");
      } catch (error) {
        alert("There was an error submitting the form.");
      }
    }
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <div>
      <h1>Welcome to the Roommate Survey!</h1>
      <HabitsAndPreferences />
      <form onSubmit={handleSubmit}>
        <div className="form-input">
          <label htmlFor="l-smoke">Live with a smoker?:</label>
          <input
            type="text"
            id="l-smoke"
            name="l-smoke"
            value={formData["l-smoke"]}
            onChange={handleChange}
          />
        </div>

        <div className="form-input">
          <label htmlFor="smoke">Do you smoke?:</label>
          <input
            type="text"
            id="smoke"
            name="smoke"
            value={formData.smoke}
            onChange={handleChange}
          />
        </div>

        <div className="form-input">
          <label htmlFor="l-drink">Live with a drinker?:</label>
          <input
            type="text"
            id="l-drink"
            name="l-drink"
            value={formData["l-drink"]}
            onChange={handleChange}
          />
        </div>

        <div className="form-input">
          <label htmlFor="drink">Do you drink?:</label>
          <input
            type="text"
            id="drink"
            name="drink"
            value={formData.drink}
            onChange={handleChange}
            />
            </div>
            <div className="form-input">
      <label htmlFor="l-extrovert">Live with an extrovert?:</label>
      <input
        type="text"
        id="l-extrovert"
        name="l-extrovert"
        value={formData["l-extrovert"]}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="extrovert">Are you an extrovert?:</label>
      <input
        type="text"
        id="extrovert"
        name="extrovert"
        value={formData.extrovert}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="study">How often do you study at home?:</label>
      <input
        type="text"
        id="study"
        name="study"
        value={formData.study}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="sleep">What time do you usually go to sleep?:</label>
      <input
        type="text"
        id="sleep"
        name="sleep"
        value={formData.sleep}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="bedtime-school">
        What time do you usually go to bed on school nights?:
      </label>
      <input
        type="text"
        id="bedtime-school"
        name="bedtime-school"
        value={formData["bedtime-school"]}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="bedtime-weekend">
        What time do you usually go to bed on weekends?:
      </label>
      <input
        type="text"
        id="bedtime-weekend"
        name="bedtime-weekend"
        value={formData["bedtime-weekend"]}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="l-messy">Live with a messy person?:</label>
      <input
        type="text"
        id="l-messy"
        name="l-messy"
        value={formData["l-messy"]}
        onChange={handleChange}
      />
    </div>

    <div className="form-input">
      <label htmlFor="messy">Are you a messy person?:</label>
      <input
        type="text"
        id="messy"
        name="messy"
        value={formData.messy}
        onChange={handleChange}
      />
    </div>

    <button type="submit">Submit</button>
  </form>
</div>
);
};

export default MyForm;
