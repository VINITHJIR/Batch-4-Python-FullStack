import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import RegisterPage from "./pages/RegisterPage";
import LoginPage from "./pages/LoginPage";
import OverviewPage from "./pages/OverviewPage";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <div className="app-main">
        <Routes>
          {/* Default / Homepage is the Register Page as requested */}
          <Route path="/" element={<RegisterPage />} />
          <Route path="/register" element={<RegisterPage />} />

          {/* Login Page */}
          <Route path="/login" element={<LoginPage />} />

          {/* Protected Student Overview Pages */}
          <Route path="/overview" element={<OverviewPage />} />
          <Route path="/students" element={<OverviewPage />} />

          {/* Catch-all redirect to Home */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
