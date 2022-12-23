import "./Employer/style.css";
function Login() {

    const handleLogin = (e)=>{
        e.preventDefault();

        //Login API endpoint

    }
    const handleRegistration = () =>{
        // Registration API endpoint
    }
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
                required
              />
            </div>
            <div class="form-outline mb-4">
              <input
                type="password"
                class="input-field"
                placeholder="Enter password"
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

            <select>
                <option></option>
                <option></option>
                <option></option>
            </select>
            <input
              type="text"
              class="input-field"
              placeholder="Enter User Type"
              required
            />
            <input
              type="text"
              class="input-field"
              placeholder="Enter Username"
              required
            />
            <input
              type="email"
              class="input-field"
              placeholder="Email Id"
              required
            />
            <input
              type="password"
              class="input-field"
              placeholder="Enter Password"
              required
            />
            <input
              type="password"
              class="input-field"
              placeholder="Confirm Password"
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
