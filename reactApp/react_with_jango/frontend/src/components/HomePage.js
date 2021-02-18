import React, { Component } from 'react'
import CreateRoomPage from './CreateRoomPage';
import RoomJoinPage from './RoomJoinPage';
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";

export class HomePage extends Component {
    constructor(props){
        super(props);

    }
    render() {
        return (
            <Router>
                <switch>
                    <Route exact path='/'> 
                        <p> this is home page</p>
                    </Route>
                    <Route path='/join' component={RoomJoinPage }/>
                    <Route path='/create' component={CreateRoomPage }/>

                </switch>
            </Router>
        )
    }
}

export default HomePage
