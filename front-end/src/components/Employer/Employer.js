import "./style2.css";
function Employer() {
  return (
    <body>
      <div class="sidebar">
        <div class="logo-details">
          <i class="fas fa-slack"></i>
          <span class="logo_name">THE TECHNICAL UNIVERSITY OF KENYA</span>
        </div>

        <ul class="nav-links">
          <li>
            <a href="#">
              <i class="fas fa-bars"></i>
              <span class="link_name">Dashboard</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fas fa-user"></i>
              <span class="link_name">Employer</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fas fa-bell"></i>
              <span class="link_name">Notifications</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fas fa-right-to-bracket"></i>
              <span class="link_name">Log Out</span>
            </a>
          </li>
        </ul>
      </div>

      <section class="home-section">
        <nav>
          <div class="sidebar-button">
            <i class="fas fa-bars sidebarBtn"></i>
            <span class="dashboard">Employer</span>
          </div>

          <div class="profile-details">
            <img src="images/profile.jpg" alt="" />
            <span class="admin_name">Sarah Kim</span>
          </div>
        </nav>

        <div class="comment-box">
          <h2>Feedback</h2>
          <form action="#">
            <input
              type="text"
              name="student's_name"
              placeholder="STUDENT'S NAME"
            />
            <input
              type="text"
              name="department's_name"
              placeholder="DEPARTMENT'S NAME"
            />
            <textarea
              name="feedback"
              placeholder="Type your feedback here..."
            ></textarea>
            <button type="submit">Submit Feedback</button>
          </form>
        </div>
      </section>

      <script src="script.js"></script>
    </body>
  );
}

export default Employer;