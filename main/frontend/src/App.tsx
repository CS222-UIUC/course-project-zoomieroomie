import React from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Users from './components/Users';
import Main from './components/Main';
import Profile from './components/Profile';
import { Route, BrowserRouter, Routes, Navigate } from 'react-router-dom';
import './App.css';
import Preferences from './components/Preferences';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/profile" element={<Profile />} />
          <Route path="/main" element={<Main />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
         <Route path="/preferences" element={<Preferences />} />
          <Route path="/*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
