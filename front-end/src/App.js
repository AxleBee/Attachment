import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SupervisorDashboard from "./components/Supervisor/Dashboard";
import LogBookFeeback from "./components/Supervisor/logbook-feedback.";
import * as React from "react";
import { Admin, Resource } from "react-admin";
import { PostEdit, PostList, PostCreate } from "./components/Students/posts";
import { StudentDashboard } from "./components/Students/Dashboard";
import jsonServerProvider from "ra-data-json-server";
import { UserList } from "./components/Students/users";
import EmployerDashboard from "./components/Employer/Dashboard";
import Login from "./components/Login";
import Notifications from "./components/Employer/Notifications";
import Employer from "./components/Employer/Employer";
const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com");
function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route
            path="/supervisor-dashboard"
            element={<SupervisorDashboard />}
          />
          <Route path="/feedback/:id" element={<LogBookFeeback />} />
          <Route path="/employer-dashboard" element={<EmployerDashboard />} />
          <Route path="/employer-notification" element={<Notifications />} />
          <Route path="/employer-feedback" element={<Employer />} />
        </Routes>
      </Router>
      {/* <Admin dataProvider={dataProvider} dashboard={StudentDashboard}>
        <Resource
          name="posts"
          list={PostList}
          edit={PostEdit}
          create={PostCreate}
        />
        <Resource name="users" list={UserList} />
      </Admin> */}
    </>
  );
}
export default App;
