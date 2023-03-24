import React, { useState } from 'react';

function Profile() {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [description, setDescription] = useState('');
  const [hobbies, setHobbies] = useState('');
  const [dorm, setDorm] = useState('');
  const [lookingFor, setLookingFor] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Submitted: ${name} - ${age} - ${description} - ${hobbies} - ${dorm} - ${lookingFor}`);
    // TODO: Save user's profile data to database
    // TODO: Redirect user to their profile page
  };

  const handleEdit = () => {
    // TODO: Allow user to edit their profile data
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="age">Age:</label>
        <input
          type="text"
          id="age"
          value={age}
          onChange={(event) => setAge(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={(event) => setDescription(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="hobbies">Hobbies:</label>
        <textarea
          id="hobbies"
          value={hobbies}
          onChange={(event) => setHobbies(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="dorm">Preferred Dorm:</label>
        <input
          type="text"
          id="dorm"
          value={dorm}
          onChange={(event) => setDorm(event.target.value)}
        />
      </div>
      <div>
        <label htmlFor="lookingFor">Looking for:</label>
        <textarea
          id="lookingFor"
          value={lookingFor}
          onChange={(event) => setLookingFor(event.target.value)}
        />
      </div>
      <button type="submit">Save Profile</button>
      <button type="button" onClick={handleEdit}>Edit Profile</button>
    </form>
  );
}

export default Profile;