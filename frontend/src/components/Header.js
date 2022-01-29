import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link } from "react-router-dom";

function Header() {
    const { isAuthenticated, user,  logout } = useContext(AuthContext);

    if (isAuthenticated) {
        return (
            <div>
                <img src={user?.avatar?.url}></img>
                <p>Welcome, {user?.username}</p>
                <Link to='/' onClick={logout}>Logout</Link>
            </div>
        )
    }

    return (
        <div>
            <Link to='/register'>Register</Link>
            &nbsp;
            <Link to='/login'>Login</Link>
        </div>
    )
}

export default Header;
