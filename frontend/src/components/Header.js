import React from "react";
import { Link } from "react-router-dom";

function Header() {
    return (
        <div>
            <div>Main Page!</div>
            <Link to='/register'>Register</Link>
            &nbsp;
            <Link to='/login'>Login</Link>
        </div>
    )
}

export default Header;
