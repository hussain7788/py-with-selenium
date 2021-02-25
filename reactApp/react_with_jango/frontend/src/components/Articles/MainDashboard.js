import React, { Component } from 'react';
import AddArticle from './AddArticle';
import ViewArticle from './ViewArticle';
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import Home from './Home';


export class MainDashboard extends Component {
    render() {
        return (
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
                        <Link to={'/add'} className="nav-link">
                                    <span>Add Articles</span>
                        </Link>
                    </li>
                    <li className="nav-item">
                    <Link to={'/view'} className="nav-link">
                                    <span>View Articles</span>
                        </Link>
                    </li>
                    
                </ul>
                </div>
            </div>
        </nav>
        )
    }
}

export default MainDashboard
