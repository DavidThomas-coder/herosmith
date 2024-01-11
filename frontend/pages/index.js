
// frontend/pages/index.js

import React from 'react';
import CreateCharacterForm from '../components/CreateCharacterForm';
import SignUpForm from '../components/SignUpForm';
import LoginForm from '../components/LoginForm';

const Home = () => {
  return (
    <div>
      <h1>Welcome to HeroSmith</h1>
      <p>Build your characters and embark on epic adventures!</p>
      <CreateCharacterForm />
      <SignUpForm />
      <LoginForm />
    </div>
  );
};

export default Home;

