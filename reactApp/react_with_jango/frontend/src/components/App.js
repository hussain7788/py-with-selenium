import React, { Component, Fragment } from 'react'
import {render} from "react-dom";
import MainDashboard from './Articles/MainDashboard';
import HomePage from './HomePage';
import JoinPage from './JoinPage';
import Header from './layout/Header';
import Dashboard from './leads/Dashboard';
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import AddArticle from './Articles/AddArticle';
import ViewArticle from './Articles/ViewArticle';
import Home from './Articles/Home';


export default class App extends Component {
    constructor(props){
        super(props);

        this.state ={
            name : "hussain",
            age : 23,
            email : "myemail.com"
        }

    }
    render() {
        return (
            // <div className="container">
            //    <MainDashboard/>
            // </div>
             <Router>
                <switch>
                    <MainDashboard/>
                    <Route exact path='/'> 
                            <Home/>
                    </Route>
                    <Route path='/add' component={AddArticle}/>
                    <Route path='/view' component={ViewArticle}/>

                </switch>
            </Router>
          
        )
    }
}
const appDiv = document.getElementById("app");
render(<App />, appDiv);
