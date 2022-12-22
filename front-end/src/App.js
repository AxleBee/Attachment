import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SupervisorDashboard from "./components/Supervisor/Dashboard";
import LogBookFeeback from "./components/Supervisor/logbook-feedback.";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route
            path="/supervisor-dashboard"
            element={<SupervisorDashboard />}
          />
          <Route path="/feedback/:id" element={<LogBookFeeback />} />
        </Routes>
      </Router>
      
    </>
  );
}
export default App;
