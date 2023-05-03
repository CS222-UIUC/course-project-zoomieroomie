import React from 'react';
import '../css/form_style.css';
import { Link } from "react-router-dom";
import MyForm from "./form_script";

interface Question {
  label: string;
  question: string;
  options: { value: string; label: string }[];
}

const HabitsAndPreferences: React.FC = () => {
  const questions: Question[] = [
    {
      label: 'l-smoke',
      question: 'Live with someone who smokes?:',
      options: [
        { value: 'often', label: '1' },
        { value: 'sometimes', label: '2' },
        { value: 'never', label: '3' }
      ],
    },
    {
      label: 'smoke',
      question: 'I smoke:',
      options: [
        { value: 'often', label: '1' },
        { value: 'sometimes', label: '2' },
        { value: 'never', label: '3' }
      ],
    },
    {
      label: 'l-drink',
      question: 'I am willing to live with someone who drinks:',
      options: [
        { value: 'yes', label: '1' },
        { value: 'no', label: '2' },
        { value: 'maybe', label: '3' }
      ],
    },
    {
      label: 'drink',
      question: 'I drink:',
      options: [
        { value: 'often', label: '1' },
        { value: 'sometimes', label: '2' },
        { value: 'never', label: '3' }
      ],
    },
    {
      label: 'extrovert',
      question: 'On a scale of 1 to 5, I describe myself as:',
      options: [
        { value: 'extremely introverted', label: '1' },
        { value: 'introverted', label: '2' },
        { value: 'neutral', label: '3' },
        { value: 'extroverted', label: '4' },
        { value: 'extremely extroverted', label: '5' }
      ],
    },
    {
      label: 'l-extrovert',
      question: 'On a scale of 1 to 5, I get along best with people who are:',
      options: [
        { value: 'extremely introverted', label: '1' },
        { value: 'introverted', label: '2' },
        { value: 'neutral', label: '3' },
        { value: 'extroverted', label: '4' },
        { value: 'extremely extroverted', label: '5' }
      ],
    },
    //ADD NEW QUESTIONS HERE
    //FORMAT: new question("label", "question", ["1", "2", "3", "4", "5"]),
    //new question("", "", ["1", "2", "3", "4", "5"]),
    {
      label: 'study',
      question: 'On a scale of 1 to 5, I prefer an in-room study environment that is:',
      options: [
        { value: 'completely quiet', label: '1' },
        { value: '', label: '2' },
        { value: 'no difference', label: '3' },
        { value: '', label: '4' },
        { value: 'never quiet -- i.e. friends in room, music playing, etc', label: '5' }
      ],
    },
    {
      label: 'sleep',
      question: 'On a scale of 1 to 5, I prefer a sleep environment that:',
      options: [
        { value: 'completely quiet', label: '1' },
        { value: '', label: '2' },
        { value: 'no difference', label: '3' },
        { value: '', label: '4' },
        { value: 'never quiet -- i.e. friends in room, music playing, etc', label: '5' }
      ],
    },
    {
      label: 'bedtime-school',
      question: 'On a school night, I typically go to bed:',
      options: [
        { value: 'before 10pm', label: '1' },
        { value: '10-11pm', label: '2' },
        { value: '11pm-12am', label: '3' },
        { value: '12am-1am', label: '4' },
        { value: '1am or after', label: '5' }
      ],
    },
    {
      label: 'bedtime-weekend',
      question: 'On the weekends, I typically go to bed:',
      options: [
        { value: 'before 10pm', label: '1' },
        { value: '10-11pm', label: '2' },
        { value: '11pm-12am', label: '3' },
        { value: '12am-1am', label: '4' },
        { value: '1am or after', label: '5' }
      ],
    },
    {
      label: 'messy',
      question: 'On a scale of 1 to 5, I describe my neatness level as:',
      options: [
        { value: 'extremely clean', label: '1' },
        { value: '', label: '2' },
        { value: 'neutral', label: '3' },
        { value: '', label: '4' },
        { value: 'extremely messy', label: '5' }
      ],
    },
    {
      label: 'l-messy',
      question: 'On a scale of 1 to 5, I prefer to live with someone whose neatness level is:',
      options: [
        { value: 'extremely clean', label: '1' },
        { value: '', label: '2' },
        { value: 'neutral', label: '3' },
        { value: '', label: '4' },
        { value: 'extremely messy', label: '5' }
      ],
    },
    ];
    
    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // HANDLE FORM SUBMISSION HERE
    };
    
    return (
    <div className="form-container">
    <h1>Habits and Preferences</h1>
    <form onSubmit={handleSubmit}>
    {questions.map((question) => (
    <div key={question.label} className="form-group">
    <label htmlFor={question.label}>{question.question}</label>
    <select id={question.label} name={question.label} required>
    {question.options.map((option) => (
      <option key={option.value} value={option.value}>
        {option.label}
      </option>
    ))}
    </select>
    </div>
    ))}
    
    <button type="submit">
    <Link to="/Main">Submit</Link>
    </button>
    
    </form>
    </div>
    );
    };
    
    export default HabitsAndPreferences;