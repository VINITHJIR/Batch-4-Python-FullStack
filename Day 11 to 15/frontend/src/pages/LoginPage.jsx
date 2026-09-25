import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
// Import common API URL from centralized config (NO hardcoded URLs)
import { LOGIN_USER_API } from "../config/api";
import "./AuthPages.css";

const LoginPage = () => {
  const navigate = useNavigate();
  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccessMsg(null);

    if (!credentials.email || !credentials.password) {
      setError("Please enter both email and password.");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch(LOGIN_USER_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: credentials.email.trim(),
          password: credentials.password,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Login failed. Please check your credentials.");
      }

      // Store JWT access token & user information in localStorage
      localStorage.setItem("access_token", data.access_token);
      if (data.user) {
        localStorage.setItem("user_info", JSON.stringify(data.user));
      }

      setSuccessMsg("Login successful! Redirecting to student overview...");

      // Navigate to Student Overview page
      setTimeout(() => {
        navigate("/overview");
      }, 800);
    } catch (err) {
      console.error("Login error:", err);
      setError(err.message || "Invalid email or password.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <div className="auth-header">
          <div className="auth-brand">🎓 Batch 4 Portal</div>
          <h1>Welcome Back</h1>
          <p>Login with your registered email and password</p>
        </div>

        {error && (
          <div className="auth-alert auth-alert-error">
            <span>⚠️ {error}</span>
          </div>
        )}

        {successMsg && (
          <div className="auth-alert auth-alert-success">
            <span>✓ {successMsg}</span>
          </div>
        )}

        <form onSubmit={handleLogin} className="auth-form">
          <div className="auth-group">
            <label>Email Address</label>
            <input
              type="email"
              name="email"
              placeholder="e.g. kavitha.raj@gmail.com"
              value={credentials.email}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="auth-group">
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder="••••••••"
              value={credentials.password}
              onChange={handleInputChange}
              required
            />
          </div>

          <button
            type="submit"
            className="btn-auth-submit"
            disabled={loading}
          >
            {loading ? "Authenticating..." : "Sign In"}
          </button>
        </form>

        <div className="auth-footer">
          Don't have an account yet?
          <Link to="/" className="auth-link">
            Register here
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
