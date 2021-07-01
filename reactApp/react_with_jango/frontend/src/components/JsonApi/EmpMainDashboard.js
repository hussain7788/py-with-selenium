import React from 'react'
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";

export default function EmpMainDashboard() {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
            <div className="container-fluid">
                <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link to={'/'} className="nav-link active">
                            <span>Home</span>
                        </Link>
                    </li>
                    <li className="nav-item">
                        <Link to={'/add_emp'} className="nav-link">
                                    <span>Add Emp</span>
                        </Link>
                    </li>
                    <li className="nav-item">
                    <Link to={'/view_emp'} className="nav-link">
                                    <span>View Emp</span>
                        </Link>
                    </li>
                    
                </ul>
                </div>
            </div>
        </nav>
        </div>
    )
}
