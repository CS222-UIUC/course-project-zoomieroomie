// Login.tsx

import React, { useState, } from 'react';
import '../css/Login.css';

interface LoginFormData {
    email: string;
    password: string;
  }

const Login: React.FC = () => {
  const [formData, setFormData] = useState<LoginFormData>({ email: '', password: '' });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
        const response = await fetch('http://127.0.0.1:5001/login', {
            method: 'POST',
            mode: 'cors',
            headers: { 
            'Content-Type': 'application/json',
           },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        console.log(response)
        if (response.ok) {
            alert('Login successful!');
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error(error);
        alert('An error occurred while logging in. Please try again later.');
    } 
  };

  return (
    <div className="login-container">
      <div className="logo-container">
        <h1>Zoomie Roomie</h1>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="form-input">
          <label htmlFor="username">Email:</label>
          <input type="text" id="username" name="email" value={formData.email} onChange={handleChange} />
        </div>
        <div className="form-input">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};


export default Login;

