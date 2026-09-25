import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
// Import common API URL from centralized config (NO hardcoded URLs)
import { REGISTER_USER_API } from "../config/api";
import "./AuthPages.css";

const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phonenumber: "",
    password: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccessMsg(null);

    // Basic Validation
    if (!formData.name || !formData.email || !formData.phonenumber || !formData.password) {
      setError("Please fill in all registration fields.");
      return;
    }

    if (formData.password.length < 6) {
      setError("Password must be at least 6 characters long.");
      return;
    }

    setLoading(true);
    try {
      const payload = {
        name: formData.name.trim(),
        email: formData.email.trim(),
        phonenumber: parseInt(formData.phonenumber, 10),
        password: formData.password,
      };

      const response = await fetch(REGISTER_USER_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Registration failed. Please try again.");
      }

      setSuccessMsg("Account created successfully! Redirecting to login page...");
      
      // Auto-navigate to login page after short delay
      setTimeout(() => {
        navigate("/login");
      }, 1500);
    } catch (err) {
      console.error("Registration error:", err);
      setError(err.message || "An error occurred while creating your account.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <div className="auth-header">
          <div className="auth-brand">🎓 Batch 4 Portal</div>
          <h1>Create Account</h1>
          <p>Register as a new user to access the Student Portal</p>
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

        <form onSubmit={handleRegister} className="auth-form">
          <div className="auth-group">
            <label>Full Name *</label>
            <input
              type="text"
              name="name"
              placeholder="e.g. Kavitha Raj"
              value={formData.name}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="auth-group">
            <label>Email Address *</label>
            <input
              type="email"
              name="email"
              placeholder="e.g. kavitha.raj@gmail.com"
              value={formData.email}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="auth-group">
            <label>Phone Number *</label>
            <input
              type="number"
              name="phonenumber"
              placeholder="e.g. 9876543210"
              value={formData.phonenumber}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="auth-group">
            <label>Password * (min. 6 characters)</label>
            <input
              type="password"
              name="password"
              placeholder="••••••••"
              value={formData.password}
              onChange={handleInputChange}
              required
            />
          </div>

          <button
            type="submit"
            className="btn-auth-submit"
            disabled={loading}
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>
        </form>

        <div className="auth-footer">
          Already have an account?
          <Link to="/login" className="auth-link">
            Sign In here
          </Link>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
