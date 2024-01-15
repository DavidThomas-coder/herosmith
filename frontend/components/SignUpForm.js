// frontend/components/SignUpForm.js

import React, { useState } from 'react';
import axios from 'axios';

const SignUpForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSignUp = async () => {
    try {
      await axios.post('http://127.0.0.1:5000/api/register', { username, password });
      // Optionally: Redirect to login or provide feedback to the user
    } catch (error) {
      console.error('Error registering user:', error);
      // Optionally: Handle error and provide feedback to the user
    }
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <label>
        Username:
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </label>
      <label>
        Password:
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </label>
      <button onClick={handleSignUp}>Sign Up</button>
    </div>
  );
};

export default SignUpForm;

