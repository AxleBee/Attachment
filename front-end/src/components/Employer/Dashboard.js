import React from "react";
import "./sytle1.css";

const EmployerDashboard = () => {
  //   let sidebar = document.querySelector(".sidebar");
  //   let sidebarBtn = document.querySelector(".sidebarBtn");

  //   sidebarBtn.onclick = function () {
  //     sidebar.classList.toggle("active");
  //   };

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
            <span class="dashboard">Dashboard</span>
          </div>
          <div class="search-box">
            <input type="text" placeholder="search..." />
            <i class="fas fa-search"></i>
          </div>
          <div class="profile-details">
            <img src="images/profile.jpg" alt="" />
            <span class="admin_name">Sarah Kim</span>
          </div>
        </nav>

        <div class="home-content">
          <div class="overview-boxes">
            <div class="box">
              <div class="left-side">
                <div class="box_topic">Departments</div>
                <div class="number">15</div>
                <div class="indicator">
                  <i class="fas fa-arrow-up arrow-up"></i>
                  <span class="text">up since 2010</span>
                </div>
              </div>
              <i class="fas fa-building building"></i>
            </div>
            <div class="box">
              <div class="left-side">
                <div class="box_topic">Employees</div>
                <div class="number">2000</div>
                <div class="indicator">
                  <i class="fas fa-arrow-up arrow-up"></i>
                  <span class="text">up since 2021</span>
                </div>
              </div>
              <i class="fas fa-user user"></i>
            </div>
            <div class="box">
              <div class="left-side">
                <div class="box_topic">Interns</div>
                <div class="number">50</div>
                <div class="indicator">
                  <i class="fas fa-arrow-up arrow-up"></i>
                  <span class="text">up since sept 2021</span>
                </div>
              </div>
              <i class="fas fa-user user2"></i>
            </div>
            <div class="box">
              <div class="left-side">
                <div class="box_topic">Projects</div>
                <div class="number">27</div>
                <div class="indicator">
                  <i class="fas fa-arrow-up arrow-up"></i>
                  <span class="text">up since may 2021</span>
                </div>
              </div>
              <i class="fas fa-p p"></i>
            </div>
          </div>

          <div class="interns-boxes">
            <div class="recent-intern box">
              <div class="title">Recent Interns</div>
              <div class="interns-details">
                <ul class="details">
                  <li class="topic">Date</li>
                  <li>
                    <a href="#">02 Oct '22</a>
                  </li>
                  <li>
                    <a href="#">02 Oct '22</a>
                  </li>
                  <li>
                    <a href="#">02 Oct '22</a>
                  </li>
                  <li>
                    <a href="#">25 0ct '22</a>
                  </li>
                  <li>
                    <a href="#">28 Oct '22</a>
                  </li>
                  <li>
                    <a href="#">02 Nov '22</a>
                  </li>
                  <li>
                    <a href="#">02 Nov '22</a>
                  </li>
                  <li>
                    <a href="#">06 Nov '22</a>
                  </li>
                  <li>
                    <a href="#">08 Nov '22</a>
                  </li>
                  <li>
                    <a href="#">08 Nov '22</a>
                  </li>
                </ul>
                <ul class="details">
                  <li class="topic">Name</li>
                  <li>
                    <a href="#">Mary Robbins</a>
                  </li>
                  <li>
                    <a href="#">John Samuel</a>
                  </li>
                  <li>
                    <a href="#">Alex Kane</a>
                  </li>
                  <li>
                    <a href="#">Anne Jacob</a>
                  </li>
                  <li>
                    <a href="#">Steve Rob</a>
                  </li>
                  <li>
                    <a href="#">Anisa Waheed</a>
                  </li>
                  <li>
                    <a href="#">Mohammed Nur</a>
                  </li>
                  <li>
                    <a href="#">Anthony Sid</a>
                  </li>
                  <li>
                    <a href="#">Zara Hassan</a>
                  </li>
                  <li>
                    <a href="#">Andrew Tate</a>
                  </li>
                </ul>
                <ul class="details">
                  <li class="topic">Email</li>
                  <li>
                    <a href="#">Mary001@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Sam302@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Kane172@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Anne642@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Stev909@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Anisa701@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Moha549@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Sid105@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Zara730@gmail.com</a>
                  </li>
                  <li>
                    <a href="#">Tate267@gmail.com</a>
                  </li>
                </ul>
                <ul class="details">
                  <li class="topic">Registration Number</li>
                  <li>
                    <a href="#">SCEE/00524/2017</a>
                  </li>
                  <li>
                    <a href="#">SCII/00838/2019</a>
                  </li>
                  <li>
                    <a href="#">AIIQ/00664/2018</a>
                  </li>
                  <li>
                    <a href="#">SCCI/00534/2017</a>
                  </li>
                  <li>
                    <a href="#">EMME/00639/2019</a>
                  </li>
                  <li>
                    <a href="#">COI/00413/2016</a>
                  </li>
                  <li>
                    <a href="#">EMME/00724/2016</a>
                  </li>
                  <li>
                    <a href="#">SCEE/01456/2018</a>
                  </li>
                  <li>
                    <a href="#">SMSI/01048/2018</a>
                  </li>
                  <li>
                    <a href="#">SCIE/02149/2015</a>
                  </li>
                </ul>
              </div>
              <div class="button">
                <a href="#">View All</a>
              </div>
            </div>

            <div class="workshops-intern box">
              <div class="title">Workshops</div>
              <ul>
                <li>
                  <a href="">
                    <img src="../Assets/Saf.jpg" alt="" />
                    <span class="workshop_name">Safaricom House</span>
                  </a>
                  <span class="place">Westlands</span>
                </li>
                <li>
                  <a href="#">
                    <img src="../Assets/agile.jpg" alt="" />
                    <span class="workshop_name">Agile Business Solutions</span>
                  </a>
                  <span class="place">Hurligham</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/adrian.jpg" alt="" />
                    <span class="workshop_name">Adrian Kenya Limited</span>
                  </a>
                  <span class="place">Embakasi</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/microsoft.jpg" alt="" />
                    <span class="workshop_name">Microsoft Kenya</span>
                  </a>
                  <span class="place">Westlands</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/avaya.jpg" alt="" />
                    <span class="workshop_name">Avaya Nairobi</span>
                  </a>
                  <span class="place">Parklands</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/huawei.jpg" alt="" />
                    <span class="workshop_name">Huawei Kenya</span>
                  </a>
                  <span class="place">Lavington</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/HP-Kenya.jpg" alt="" />
                    <span class="workshop_name">HP-Kenya</span>
                  </a>
                  <span class="place">Upperhill</span>
                </li>
                <li>
                  <a href="#">
                    <img src="images/sophos.jpg" alt="" />
                    <span class="workshop_name">Sophos Kenya</span>
                  </a>
                  <span class="place">Buruburu</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </body>
  );
};

export default EmployerDashboard;

// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <link
//     rel="stylesheet"
//     href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
//     integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A=="
//     crossorigin="anonymous" referrerpolicy="no-referrer" />
//     <title>Employer Dashboard</title>
//     <link rel="stylesheet" href="sytle1.css">

// </head>