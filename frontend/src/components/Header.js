import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link } from "react-router-dom";
import '../styles/header.css';

function Header() {
  const { isAuthenticated, user,  logout } = useContext(AuthContext);

  if (isAuthenticated && user) {
    return (
      <div className="mt-1 d-flex justify-content-between align-items-center">
        <h2>GLOBE ADVENTURE</h2>
        <div class="dropdown d-flex justify-content-end">
          <span 
            className="dropdown-toggle" 
            type="button" 
            id="dropdownMenuButton" 
            data-toggle="dropdown" 
            aria-haspopup="true" 
            aria-expanded="false"
          >
            <img className="header-avatar" src={user?.avatar?.url} alt="User avatar"></img>
          </span>
          
          <div className="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuButton">
            <span className="dropdown-item">Welcome, {user?.username}</span>
            <div className="dropdown-divider" />
            <Link className="dropdown-item" to='/' onClick={logout}>Logout</Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="mt-1 d-flex justify-content-between">
        <h2>GLOBE ADVENTURE</h2>
        <div>
          <Link className='btn btn-success' to='/register'>Register</Link>
          &nbsp;
          <Link class='btn btn-primary' to='/login'>Login</Link>
        </div>
    </div>
  )
}

export default Header;
