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
import AddEmp from './JsonApi/AddEmp';
import ViewEmp from './JsonApi/ViewEmp';
import EmpMainDashboard from './JsonApi/EmpMainDashboard';



export default class App extends Component {
    constructor(props){
        super(props);

        this.state ={
            name : "hussain",
            age : 23,
            email : "myemail.com"
        }

    }
    sample(data){
        console.log("parent data::",data)
    }
    render() {
        return (
             <Router>
                    {/* <MainDashboard/> */}
                    <EmpMainDashboard/>
                <switch>
                    <Route exact path='/'> 
                            <Home/>
                    </Route>
                    {/* <Route path='/add' render={(props) => <AddArticle {...props} sample={this.sample} />} />
                    <Route path='/view' component={ViewArticle}/> */}
                    <Route path='/add_emp' render={(props) => <AddEmp {...props} data="Add Emp" />} />
                    <Route path="/view_emp"  render={(props) => <ViewEmp {...props} data="View Emp" />} />

                </switch>
            </Router>
          
        )
    }
}
const appDiv = document.getElementById("app");
render(<App />, appDiv);
