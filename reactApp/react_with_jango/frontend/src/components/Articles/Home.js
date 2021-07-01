import React, { Component } from 'react'
import AddArticle from './AddArticle'
import MainDashboard from './MainDashboard'
import ViewArticle from './ViewArticle'
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import { blueGrey } from '@material-ui/core/colors';


export class Home extends Component {
    constructor(){
        super()
        this.state = {
            "name":"Hussain",
            "add": "hyderabad"
        }
    }
    render() {
        return (
            <div className="container">
                <h1 style={{color:'green', fontSize:'40px',}}>Welcome</h1>
                <img src="static/images/login.png"></img>
                <h1 style={{color:"red", fontSize:"30px", border:0, margin:0, fontFamily:"blueGrey"}}>Name :: {this.state.name}</h1>
                <h1 style={{fontSize:"35px"}}>Address :: {this.state.add}</h1>

            </div>

           
        )
    }
}

export default Home
