import React, { useState } from "react";
import axios from "axios";

export const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isLogin, setIsLogin] = useState(true);

  // Submit form
  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      if (!username || !password) {
        setErrorMessage("Both username and password are required");
        return;
      }

      // If login
      if (isLogin) {
        const response = await axios.post("http://127.0.0.1:8000/users/login", {
          username: username,
          password: password,
        });

        if (response.status === 200) {
          alert("Login successful!");
          setErrorMessage("");
          // Redirection to another page
        } else {
          setErrorMessage("Invalid username or password");
        }
      } else {
        // If register
        const response = await axios.post("http://127.0.0.1:8000/users/register", {
          username: username,
          password: password,
        });

        if (response.status === 201) {
          alert("Registration successful! You can now log in.");
          setIsLogin(true);
          setErrorMessage("");
        } else {
          setErrorMessage("Error registering user");
        }
      }
    } catch (error) {
      setErrorMessage("Username already exists");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">
          {isLogin ? "Log in" : "Register"}
        </button>
      </form>

      {errorMessage && <div style={{ color: "red" }}>{errorMessage}</div>}

      <div>
        <button onClick={() => setIsLogin(!isLogin)}>
          {isLogin ? "Need an account? Register here" : "Already have an account? Log in"}
        </button>
      </div>
    </div>
  );
};
