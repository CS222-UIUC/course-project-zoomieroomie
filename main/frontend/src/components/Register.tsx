//Register.tsx

import React, { useState } from "react";
import "../css/Register.css";
import { Link } from "react-router-dom";

interface RegisterFormData {
  firstName: string;
  lastName: string;
  email: string;
  password: string;
  confirmPassword: string;
}

const Register: React.FC = () => {
  const [formData, setFormData] = useState<RegisterFormData>({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const proxyUrl = 'https://proxy.cors.sh/';
  const apiUrl = 'http://127.0.0.1:5001/register';

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!formData.firstName) {
      alert("Please enter your first name.");
      return;
    }
    if (!formData.lastName) {
      alert("Please enter your last name.");
      return;
    }
    const emailPattern = /^[^\s@]+@illinois\.edu$/;
    if (!emailPattern.test(formData.email)) {
      alert("Please enter a valid @illinois.edu email address.");
      return;
    }
    
    const passwordPattern = /^(?=.*[A-Z].)(?=.*\d)(?=.*[!@#$%^&*])(?=.{7,})/;

    if (!passwordPattern.test(formData.password)) {
      alert(
        'Please enter a password that is at least 8 characters long and contains at least 1 capital letter, at least 1 number, and at least 1 special character from the list: "!,@,#,$<%,&,*".'
      );
      return;
    }
    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    (async () => {
      try {
        const response = await fetch(proxyUrl + apiUrl, {
          method: 'POST',
          mode: 'cors',
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        })
        .then(response => {
          // alert(response.ok);
          // if (response.ok) {
          //   window.location.href = '/main';
          // }
          window.location.href = '/main';
        })
        .catch(error => {
          alert("There was an error creating a user.");
        });
      } catch (error) {
        alert('There was an error connecting to the database.');
      }
    })();
  };

  return (
    <div>
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="firstName">First Name:</label>
          <input
            type="text"
            id="firstName"
            name="firstName"
            value={formData.firstName}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="lastName">Last Name:</label>
          <input
            type="text"
            id="lastName"
            name="lastName"
            value={formData.lastName}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="text"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;