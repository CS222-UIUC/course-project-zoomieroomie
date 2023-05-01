// Users.tsx

import React, { useEffect, useState } from 'react';

interface User {
  email: string;
  password: string;
  firstname: string;
  lastname: string;
}

const Users: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    const getUsers = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5001/users', {
          method: 'GET',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
        });
        const data = await response.json();
        setUsers(data.users);
      } catch (error) {
        console.error(error);
        alert('An error occurred while fetching the users. Please try again later.');
      }
    };
    getUsers();
  }, []);

  return (
    <div>
      <h1>Users</h1>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <ul>
          {users.map((user) => (
            <li key={`${user.email}-${user.password}`}>
              <p>Email: {user.email}</p>
              <p>First Name: {user.firstname}</p>
              <p>Last Name: {user.lastname}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Users;
