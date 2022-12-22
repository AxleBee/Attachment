import React from "react";
import { useEffect, useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";

function SupervisorDashboard() {
  //Back to top button
  const [backToTopButton, setBackToTopButton] = useState(false);
  useEffect(() => {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 100) {
        setBackToTopButton(true);
      } else {
        setBackToTopButton(false);
      }
    });
  }, []);

  const scrollup = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  // fetching api data
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch(
      "https://api.themoviedb.org/3/movie/popular?api_key=1a612bf729e479b9f236c64a3ddeb94b"
    )
      .then((response) => response.json())
      .then((data) => {
        setMovies(data["results"]);
      });
  }, []);

  // Authentication
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(null);
  useEffect(() => {
    const loggedInUser = localStorage.getItem("authenticated");
    if (loggedInUser) {
      setIsAuthenticated(loggedInUser);
    }
  }, []);

  const logOut = () => {
    localStorage.clear();
    navigate("/", { replace: true });
  };

  if (!isAuthenticated) {
    navigate("/", { replace: true });
    // <Navigate replace={true} to={"/supervisor-dashboard"}/>
  } else {
    return (
      <div class="continer-fluid">
        <div class=" wrapper">
          {/* <!-- Sidebar  --> */}
          <nav id="sidebar">
            <div class="sidebar-header">
              <h3>Dashboard</h3>
            </div>

            <ul class="list-unstyled components">
              <img
                id="profile-pic"
                src="https://mdbootstrap.com/img/new/avatars/8.jpg"
                alt=""
                style={{ width: "45px", height: "45px" }}
                class="rounded-circle m-3"
              />
              <li>
                <a href="#">
                  <i class="fa fa-user" aria-hidden="true"></i>&nbsp;&nbsp;
                  Profile
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa fa-book" aria-hidden="true"></i>&nbsp;&nbsp;
                  Logbooks
                </a>
              </li>
            </ul>
          </nav>

          {/* <!-- Page Content  --> */}
          <div id="content" class="m-3">
            <nav class="navbar  navbar-light bg-light">
              <div class="container-fluid">
                <button
                  type="button"
                  id="sidebarCollapse"
                  class="btn badge-success"
                  title="Collapse"
                >
                  <span>
                    {" "}
                    <i class="fas fa-align-justify"></i>
                  </span>
                </button>
                <div class="dropdown">
                  <button
                    class="btn btn-secondary dropdown-toggle"
                    type="button"
                    id="dropdownMenuButton"
                    data-toggle="dropdown"
                    aria-haspopup="true"
                    aria-expanded="false"
                  ></button>
                  <div
                    class="dropdown-menu"
                    aria-labelledby="dropdownMenuButton"
                  >
                    <button class="dropdown-item" onClick={logOut}>
                      <i class="fa fa-sign-out" aria-hidden="true"></i>
                      &nbsp;&nbsp; Logout
                    </button>
                  </div>
                </div>
              </div>
            </nav>
            <h2>Submissions</h2>

            {/* data table */}
            <table class="table align-middle mb-0 bg-white w-auto ">
              <thead class="bg-light">
                <tr>
                  <th>Student Name</th>
                  <th>Title</th>
                  <th>Organistion</th>
                  <th>Activity</th>
                </tr>
              </thead>
              <tbody>
                {movies.map((movie, index) => {
                  return (
                    <tr key={index}>
                      <td>
                        <div class="d-flex align-items-center">
                          <img
                            // src="https://mdbootstrap.com/img/new/avatars/8.jpg"
                            src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
                            alt=""
                            style={{ width: "45px", height: "45px" }}
                            class="rounded-circle"
                          />
                          <div class="ms-3">
                            <p class="fw-bold mb-1">{movie.id}</p>
                            <p class="text-muted mb-0">john.doe@gmail.com</p>
                          </div>
                        </div>
                      </td>
                      <td>
                        <div class="d-flex align-items-center">
                          {movie.title}
                        </div>
                      </td>
                      <td>
                        <p class="fw-normal mb-1">Software engineer</p>
                        <p class="text-muted mb-0">IT department</p>
                      </td>
                      <td>
                        <a
                          href={`/feedback/${movie.id}`}
                          class="badge badge-success rounded-pill d-inline"
                        >
                          view
                        </a>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        {backToTopButton && (
          <button onClick={scrollup} id="back-to-top" className="btn">
            {" "}
            Back Top &nbsp;
            <i class="fa fa-arrow-circle-up" aria-hidden="true"></i>
          </button>
        )}
      </div>
    );
  }
}

export default SupervisorDashboard;
