import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import Users from './components/Users';
import Main from './components/Main';

import './App.css';

function App() {
  return (
    <div className="App">
      <Routes>
               <Route path="/Login">
                  <Route index element={<Login />} />
               </Route>
               <Route path="/Register">
                  <Route index element={<Register />} />
               </Route>
               <Route path="/Main">
                  <Route index element={<Main />} />
               </Route>
               <Route path="/User">
                  <Route index element={<User />} />
               </Route>
            </Routes>
    </div>
  );
}

export default App;
