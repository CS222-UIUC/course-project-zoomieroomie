import React, { useState } from 'react';

function MainPage() {
  const [questions, setQuestions] = useState<string[]>([
    'Do you stay up late at night?',
    'Do you take academics very seriously?',
    'Do you like to party?',
    'Are you very religious?',
    'Do you enjoy working out?',
    'Do you want lights out by a certain time at night?',
    'Are you okay with other people being in your dorm, like your roommates friends?',
  ]);

  const [answers, setAnswers] = useState<boolean[]>(Array(questions.length).fill(null));

  const handleAnswer = (index: number, answer: boolean) => {
    const newAnswers = [...answers];
    newAnswers[index] = answer;
    setAnswers(newAnswers);
  };

  return (
    <div>
      <h1>Questions</h1>
      <ul>
        {questions.map((question, index) => (
          <li key={index}>
            {question}
            <div>
              <button onClick={() => handleAnswer(index, true)}>Yes</button>
              <button onClick={() => handleAnswer(index, false)}>No</button>
            </div>
          </li>
        ))}
      </ul>
      <h2>Answers:</h2>
      <ul>
        {answers.map((answer, index) => (
          <li key={index}>{answer === null ? '-' : answer ? 'Yes' : 'No'}</li>
        ))}
      </ul>
    </div>
  );
}

export default MainPage;