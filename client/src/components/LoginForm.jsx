import React, { useState } from "react";
import axios from "axios";
import "./LoginForm.css";

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
    
      if (isLogin) {
        // Login request
        const response = await axios.post("http://127.0.0.1:8000/users/login", {
          username: username,
          password: password,
        });

        const token = response.data.token;

        // Save token to local storage
        localStorage.setItem("token", token);
        
        alert("Login successful!");
        setErrorMessage("");
        // Redirect to another page
      } else {
        // Register request
        await axios.post("http://127.0.0.1:8000/users/register", {
          username: username,
          password: password,
        });
        alert("Registration successful! You can now log in.");
        setIsLogin(true);
        setErrorMessage("");
      }
    } catch (error) {
      if (error.response) {
        // Handle specific HTTP errors
        if (error.response.status === 400) {
          setErrorMessage(
            isLogin ? "Invalid username or password" : "Error registering user"
          );
        } else {
          setErrorMessage("An unexpected error occurred");
        }
      } else if (error.request) {
        // Request was made but no response was received
        setErrorMessage("Server is not responding. Please try again later.");
      } else {
        // Something else caused the error
        console.log("Error", error.message);
        setErrorMessage("An unexpected error occurred");
      }
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

      {errorMessage && <div>{errorMessage}</div>}

      <div>
        <button onClick={() => setIsLogin(!isLogin)}>
          {isLogin ? "Need an account? Register here" : "Already have an account? Log in"}
        </button>
      </div>
    </div>
  );
};
