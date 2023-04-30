// Preferences.tsx

import React, { useEffect, useState } from 'react';

interface Preference {
    user: string
}

const Preferences: React.FC = () => {
  const [preferences, setPreferences] = useState<Preference[]>([]);

  useEffect(() => {
    const getPreferences = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5001/preferences', {
          method: 'GET',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
        });
        const data = await response.json();
        setPreferences(data.preferences);
      } catch (error) {
        console.error(error);
        alert('An error occurred while fetching the user preferences. Please try again later.');
      }
    };
    getPreferences();
  }, []);

  return (
    <div>
      <h1>Users that have submitted Preferences:</h1>
      {preferences.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul>
          {preferences.map((preference) => (
            <li key={preference.user}>
              <p>User: {preference.user}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Preferences;
