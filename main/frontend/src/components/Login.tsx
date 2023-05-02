// Login.tsx

import React, { useState } from 'react';
import '../css/Login.css';
import { Link } from "react-router-dom";

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
    
    (async () => {
      try {
        const response = await fetch('http://127.0.0.1:5001/login', {
          method: 'POST',
          mode: 'cors',
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        })
        .then(response => {
          alert("Login successful!");
        })
        .catch(error => {
          alert("There was an error logging in.");
        });
      } catch (error) {
        alert('There was an error logging in.');
      }
    })();
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
        <button type="submit">
        <Link to="/Main">Login</Link>
        </button>
        <button type="button">Don't have an account? <br />
        <Link to="/Register">Register</Link>
        </button>
      </form>
    </div>
  );
};


export default Login;