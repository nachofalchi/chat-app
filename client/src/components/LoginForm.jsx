import React, { useState } from "react";

export const LoginForm = () => {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isLoggedIn, setIsLoggedIn] = useState(false);


  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!username || !password) {
      setErrorMessage("Por favor, completa todos los campos.");
      return;
    }

  };

  return (
    <div>
      <h1>Login</h1>
      
      {errorMessage && <div style={{ color: "red" }}>{errorMessage}</div>}

      {/* Form */}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type=""
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter your username"
          />
        </div>

        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
          />
        </div>

        <button type="submit">Log In</button>
      </form>

      {isLoggedIn && <div>¡Inicio de sesión exitoso!</div>}

      <div>
        <p>Don’t have an account?</p>
        <button>Sign up</button>
      </div>
    </div>
  );
};
