import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import "./Employer/style.css";
function Login() {
  const navigate = useNavigate();
  const [authenticated, setauthenticated] = useState(
    localStorage.getItem(localStorage.getItem("authenticated") || false)
  );
  const handleLogin = (e) => {
    e.preventDefault();
    let email = document.querySelector('input[name="loginEmail"]')
      ? document.querySelector('input[name="loginEmail"]').value
      : "";
    let pass = document.querySelector('input[name="loginPassword"]')
      ? document.querySelector('input[name="loginPassword"]').value
      : "";
    //Login API endpoint
    fetch(" http://127.0.0.1:8000/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: pass,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data && data.user_type == "supervisor") {
          setauthenticated(true);
          localStorage.setItem("authenticated", true);
          navigate("/supervisor-dashboard/", { replace: true });
        }
      });
  };

  const handleRegistration = (e) => {
    e.preventDefault();
    let userType = document.querySelector("#userTypes")
      ? document.querySelector("#userTypes").value
      : "";
    let username = document.querySelector('input[name="r-username"]')
      ? document.querySelector('input[name="r-username"]').value
      : "";
    let email = document.querySelector('input[name="r-email"]')
      ? document.querySelector('input[name="r-email"]').value
      : "";
    let pass = document.querySelector('input[name="r-password"]')
      ? document.querySelector('input[name="r-password"]').value
      : "";
    let confirmPass = document.querySelector('input[name="r-confirm"]')
      ? document.querySelector('input[name="r-confirm"]').value
      : "";
    // alert([userType, username, email, pass, confirmPass])
    if (pass !== confirmPass) {
      alert("Password must match");
      return false;
    }
    // Registration API endpoint
    fetch(" http://127.0.0.1:8000/api/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        username: username,
        password: pass,
        user_type: userType,
      }),
    })
      .then((res) => {
        res.json();
        if (res.status == 201) {
          alert("Registered Successfully, Click Login to Sign in");
        }
      })
      .catch((error) => {
        console.log(error);
      });
      let form = document.querySelector("#signup")
      ? document.querySelector("#signup")
      : "";
      form.reset()
  };
  return (
    <body>
      <div class="hero">
        <div class="form-box">
          <div class="button-box">
            <div id="btn"></div>
            <button type="button" class="toggle-btn" id="myLogin">
              Login
            </button>
            <button type="button" class="toggle-btn" id="mySignUp">
              Signup
            </button>
          </div>
          <form id="login" class="input-group" onSubmit={handleLogin}>
            <div class="form-outline mb-4">
              <input
                type="email"
                class="input-field"
                placeholder="Enter Username"
                name="loginEmail"
                required
              />
            </div>
            <div class="form-outline mb-4">
              <input
                type="password"
                class="input-field"
                placeholder="Enter password"
                name="loginPassword"
                required
              />
            </div>
            <input type="checkbox" class="chech-box" />
            <span>Remember me.</span>
            <button type="submit" class="submit-btn">
              Login
            </button>
          </form>

          <form id="signup" class="input-group" onSubmit={handleRegistration}>
            <label for="userTypes">User-Type: </label>
            <select name="userTypes" id="userTypes" class="input-field">
              <option value="supervisor">Supervisor</option>
              <option value="employer">Employer</option>
              <option value="student">Student</option>
            </select>
            <input
              type="text"
              class="input-field"
              placeholder="Enter Username"
              name="r-username"
              required
            />
            <input
              type="email"
              class="input-field"
              placeholder="Email Id"
              name="r-email"
              required
            />
            <input
              type="password"
              class="input-field"
              placeholder="Enter Password"
              name="r-password"
              required
            />
            <input
              type="password"
              class="input-field"
              placeholder="Confirm Password"
              name="r-confirm"
              required
            />
            <input type="checkbox" class="chech-box" />
            <span>I agree to the terms & conditions.</span>
            <button type="submit" class="submit-btn">
              Signup
            </button>
          </form>
          <h1>ATTACHMENTS MANAGEMENT SYSTEM</h1>
        </div>
      </div>
    </body>
  );
}

export default Login;
