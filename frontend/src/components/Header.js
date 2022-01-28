import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link } from "react-router-dom";

function Header() {
    const { isAuthenticated, logout } = useContext(AuthContext);

    if (isAuthenticated) {
        return (
            <div>
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
