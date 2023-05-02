import React from 'react';
import '../css/form_style.css';
import { Link } from "react-router-dom";

interface Question {
  label: string;
  question: string;
  options: string[];
}

const HabitsAndPreferences: React.FC = () => {
  const questions: Question[] = [
    {
      label: 'l-smoke',
      question: 'I am willing to live with a smoker:',
      options: ['yes', 'no', 'maybe'],
    },
    {
      label: 'smoke',
      question: 'I smoke:',
      options: ['often', 'sometimes', 'never'],
    },
    {
      label: 'l-drink',
      question: 'I am willing to live with someone who drinks:',
      options: ['yes', 'no', 'maybe'],
    },
    {
      label: 'drink',
      question: 'I drink:',
      options: ['often', 'sometimes', 'never'],
    },
    {
      label: 'extrovert',
      question: 'On a scale of 1 to 5, I describe myself as:',
      options: ['1 (extremely introverted)', '2', '3', '4', '5 (extremely extroverted)'],
    },
    {
      label: 'l-extrovert',
      question: 'On a scale of 1 to 5, I get along best with people who are:',
      options: ['1 (extremely introverted)', '2', '3 (no difference)', '4', '5 (extremely extroverted)'],
    },
    //ADD NEW QUESTIONS HERE
    //FORMAT: new question("label", "question", ["1", "2", "3", "4", "5"]),
    //new question("", "", ["1", "2", "3", "4", "5"]),
    {
      label: 'study',
      question: 'On a scale of 1 to 5, I prefer an in-room study environment that is:',
      options: [
        '1 (completely quiet)',
        '2',
        '3 (no difference)',
        '4',
        '5 (never quiet -- i.e. friends in room, music playing, etc.)',
      ],
    },
    {
      label: 'sleep',
      question: 'On a scale of 1 to 5, I prefer a sleep environment that:',
      options: ['1 (is completely quiet)', '2', '3 (no difference)', '4', '5 (has some noise)'],
    },
    {
      label: 'bedtime-school',
      question: 'On a school night, I typically go to bed:',
      options: ['before 10pm', '10-11pm', '11am-12am', '12pm-1am', '1-2am', 'after 2am'],
    },
    {
      label: 'bedtime-weekend',
      question: 'On the weekends, I typically go to bed:',
      options: ['before 10pm', '10-11pm', '11am-12am', '12pm-1am', '1-2am', 'after 2am'],
    },
    {
      label: 'messy',
      question: 'On a scale of 1 to 5, I describe my neatness level as:',
      options: ['1 (extremely clean)', '2', '3', '4', '5 (extremely messy)'],
    },
    {
      label: 'l-messy',
      question: 'On a scale of 1 to 5, I prefer to live with someone whose neatness level is:',
      options: ['1 (extremely clean)', '2', '3 (no difference)', '4', '5 (extremely messy)'],
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
    <option key={option} value={option}>
    {option}
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