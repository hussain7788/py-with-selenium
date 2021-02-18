import React, { Component, Fragment } from 'react'
import {render} from "react-dom";
import HomePage from './HomePage';
import JoinPage from './JoinPage';
import Header from './layout/Header';
import Dashboard from './leads/Dashboard';

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
            <div className="container">
                    <JoinPage/>
                </div>

        )
    }
}
const appDiv = document.getElementById("app");
render(<App />, appDiv);
