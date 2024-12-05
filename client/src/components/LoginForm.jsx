import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "./LoginForm.css";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const LoginForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [isLogin, setIsLogin] = useState(true);
  const navigate = useNavigate();

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
        console.log({
          API_URL: process.env.REACT_APP_API_URL,
          ALL_ENV: process.env
        });
        const response = await axios.post(`${process.env.REACT_APP_API_URL}/users/login`, {
          username: username,
          password: password,
        });

        const token = response.data.token;

        // Save token to local storage
        localStorage.setItem("token", token);
        
        toast.success("Login successful!", {
          position: "top-right",
          autoClose: 1000,
        });

        // Redirection
        setTimeout(() => {
          navigate("/main");
        }, 1000);

      } else {
        // Register request
        await axios.post(`${process.env.REACT_APP_API_URL}/users/register`, {
          username: username,
          password: password,
        });
        toast.success("Registration successful! You can now log in.");
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
        setErrorMessage("An unexpected error occurred");
      }
    }
  };

  return (
    <>
      <div className="login-container">
        <div className="login-form">
          <h2>{isLogin ? "Login" : "Register"}</h2>
          <form onSubmit={handleSubmit}>
            <div className="login-form__field">
                <label className="login-form__label">
                    Username
                </label>
                <input
                  className="login-form__input"
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="Enter username"
                />
            </div>
            
            <div className="login-form__field">
                <label className="login-form__label">
                Password
                </label>
                <input
                  className="login-form__input"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter password"
                />
            </div>

            {errorMessage && (
              <div className="login-form__error">{errorMessage}</div>
            )}

            <button className="login-form__button" type="submit">
              {isLogin ? "Log in" : "Register"}
            </button>
          </form>

          <div className="login-form__toggle">
            <button
              className="login-form__toggle-button"
              onClick={() => setIsLogin(!isLogin)}
            >
              {isLogin 
                ? "Need an account? Register here" 
                : "Already have an account? Log in"}
            </button>
          </div>
        </div>
      </div>
      <ToastContainer/></>
  );
};
