import React, { useState } from 'react';
import logo512 from 'C:\Users\vinee\OneDrive - University of Illinois - Urbana\UIUC\Classes\Second sem freshman\CS 222\ZoomieRoomie\my-app\public\logo512.png';



function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  /*const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Submitted: ${username} - ${password}`);
    // TODO: Implement login logic here*/

   const handleSubmit = async (event) => {
   event.preventDefault();
   
   try {
      const response = await fetch('/api/login', {
         method: 'POST',
         headers: {
         'Content-Type': 'application/json'
         },
         body: JSON.stringify({ username, password })
      });
   
      if (response.ok) {
         console.log('Login successful!');
         // TODO: Redirect the user to the authenticated page
      } else {
         console.log('Invalid login credentials.');
      }
   } catch (error) {
      console.error('Error:', error);
   }
   }


  return (
    <div>
    <img src="./logo512.png" alt="Logo" />
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
        />
      </div>
      <button type="submit">Login</button>
    </form>
    </div>
  );
}


export default LoginPage;
