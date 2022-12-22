import logo from "./logo.svg";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SupervisorDashboard from "./components/Supervisor/Dashboard";
import LogBookFeeback from "./components/Supervisor/logbook-feedback.";
import * as React from 'react';
import{Admin,Resource} from 'react-admin';
import { PostEdit,PostList,PostCreate } from "./components/Students/posts"; 
import { StudentDashboard } from "./components/Students/Dashboard";
import jsonServerProvider from 'ra-data-json-server';
import { UserList } from "./components/Students/users";
const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com");
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
     <Admin dataProvider={dataProvider} dashboard={StudentDashboard}>
        <Resource
          name="posts"
          list={PostList}
          edit={PostEdit}
          create={PostCreate}
        />
        <Resource name="users" list={UserList} />
      </Admin>
    
    </>
  );
}
export default App;
