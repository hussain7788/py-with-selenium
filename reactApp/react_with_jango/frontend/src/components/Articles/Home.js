import React, { Component } from 'react'
import AddArticle from './AddArticle'
import MainDashboard from './MainDashboard'
import ViewArticle from './ViewArticle'
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";


export class Home extends Component {
    render() {
        return (
            <div className="container">
                <h1 style={{color:'red', fontSize:'40px',}}>This is Home</h1>
                <img src="static/images/login.png"></img>
            </div>

           
        )
    }
}

export default Home
