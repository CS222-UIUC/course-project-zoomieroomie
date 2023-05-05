import React, { useState } from "react";
import '../css/form_style.css';
import { Link } from "react-router-dom";
import MyForm from "./form_script";
import FormData from "./form_script";

interface FormData {
  
  [key: string]: {
    question: string;
    options: { value: string | ""; label: string | "" }[];
  };
}

const HabitsAndPreferences: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    "l-smoke": {
      question: "Live with someone who smokes?:",
      options: [
        { value: "often", label: "1" },
        { value: "sometimes", label: "2" },
        { value: "never", label: "3" },
      ],
    },
    smoke: {
      question: "I smoke:",
      options: [
        { value: "often", label: "1" },
        { value: "sometimes", label: "2" },
        { value: "never", label: "3" },
      ],
    },
    "l-drink": {
      question: "I am willing to live with someone who drinks:",
      options: [
        { value: "yes", label: "1" },
        { value: "no", label: "2" },
        { value: "maybe", label: "3" },
      ],
    },
    drink: {
      question: "I drink:",
      options: [
        { value: "often", label: "1" },
        { value: "sometimes", label: "2" },
        { value: "never", label: "3" },
      ],
    },
    extrovert: {
      question: "On a scale of 1 to 5, I describe myself as:",
      options: [
        { value: "extremely introverted", label: "1" },
        { value: "introverted", label: "2" },
        { value: "neutral", label: "3" },
        { value: "extroverted", label: "4" },
        { value: "extremely extroverted", label: "5" },
      ],
    },
    "l-extrovert": {
      question: "On a scale of 1 to 5, I get along best with people who are:",
      options: [
        { value: "extremely introverted", label: "1" },
        { value: "introverted", label: "2" },
        { value: "neutral", label: "3" },
        { value: "extroverted", label: "4" },
        { value: "extremely extroverted", label: "5" },
      ],
    },
    //ADD NEW QUESTIONS HERE
    //FORMAT: new question("label", "question", ["1", "2", "3", "4", "5"]),
    //new question("", "", ["1", "2", "3", "4", "5"]),
    study: {
      question: "On a scale of 1 to 5, I prefer an in-room study environment that is:",
      options: [
        { value: "completely quiet", label: "1" },
        { value: "somewhat quiet", label: "2" },
        { value: "no difference", label: "3" },
        { value: "somewhat noisy", label: "4" },
        { value: "never quiet -- i.e. friends in room, music playing, etc", label: '5' },
      ],
    },
    sleep: {
      question: "On a scale of 1 to 5, I prefer a sleep environment that:",
      options: [
        { value: 'completely quiet', label: '1' },
        { value: '', label: '2' },
        { value: 'no difference', label: '3' },
        { value: '', label: '4' },
        { value: 'never quiet -- i.e. friends in room, music playing, etc', label: '5' },
      ],
    },
    "bedtime-school": {
      question: "On a school night, I typically go to bed:",
      options: [
        { value: 'before 10pm', label: '1' },
        { value: '10-11pm', label: '2' },
        { value: '11pm-12am', label: '3' },
        { value: '12am-1am', label: '4' },
        { value: '1am or after', label: '5' },
      ],
    },

    "bedtime-weekend": {
      question: "On the weekends, I typically go to bed::",
      options: [
        { value: 'before 10pm', label: '1' },
        { value: '10-11pm', label: '2' },
        { value: '11pm-12am', label: '3' },
        { value: '12am-1am', label: '4' },
        { value: '1am or after', label: '5' },
      ],
    },
    messy: {
      question: 'On a scale of 1 to 5, I describe my neatness level as:',
      options: [
        { value: 'extremely clean', label: '1' },
        { value: '', label: '2' },
        { value: 'neutral', label: '3' },
        { value: '', label: '4' },
        { value: 'extremely messy', label: '5' },
      ],
    },
    "l-messy": {
      question: 'On a scale of 1 to 5, I prefer to live with someone whose neatness level is:',
      options: [
        { value: 'extremely clean', label: '1' },
        { value: '', label: '2' },
        { value: 'neutral', label: '3' },
        { value: '', label: '4' },
        { value: 'extremely messy', label: '5' },
      ],
    },
  }as FormData);
    
  return (
    <div className="form-container">
      <h1 className="form-header">Habits and Preferences</h1>
      <MyForm formData={formData} setFormData={setFormData} />
      <Link to="/form_script" className="submit-button">
        Submit
      </Link>
    </div>
  );
  };
    
export default HabitsAndPreferences;