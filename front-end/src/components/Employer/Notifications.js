import "./style3.css";
function Notifications() {
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
            <span class="dashboard">Notifications</span>
          </div>

          <div class="profile-details">
            <img src="images/profile.jpg" alt="" />
            <span class="admin_name">Sarah Kim</span>
          </div>
        </nav>
      </section>

      
    </body>
  );
}

export default Notifications