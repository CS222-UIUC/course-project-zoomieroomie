import React from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Users from './components/Users';
import Main from './components/Main';
import Profile from './components/Profile';
import RoommateMatches from './components/matches';
import { Route, BrowserRouter, Routes, Navigate } from 'react-router-dom';
import './App.css';
import Preferences from './components/Preferences';
import MyForm from './components/form_script';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/profile" element={<Profile />} />
          <Route path="/main" element={<Main />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/matches" element={<RoommateMatches />} />
          <Route path="/form_script" element={<MyForm />} />
         <Route path="/preferences" element={<Preferences />} />
          <Route path="/*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
