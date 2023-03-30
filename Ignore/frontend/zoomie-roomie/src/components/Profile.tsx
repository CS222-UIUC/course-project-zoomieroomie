import React, { useState } from 'react';

function Profile() {
  const [name, setName] = useState<string>('');
  const [age, setAge] = useState<number>(0);
  const [description, setDescription] = useState<string>('');
  const [hobbies, setHobbies] = useState<string>('');
  const [dorm, setDorm] = useState<string>('');
  const [lookingFor, setLookingFor] = useState<string>('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
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
          type="number"
          id="age"
          value={age}
          onChange={(event) => setAge(parseInt(event.target.value))}
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