import React, { Component } from 'react';
import {TextField, Button, Grid, Typography} from "@material-ui/core";
import {Link} from "react-router-dom";

export class JoinPage extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             roomCode : "",
             error : "hello"
        }
        this.handleFields = this.handleFields.bind(this);
        this.BtnPressed = this.BtnPressed.bind(this);
    }
    
    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                <Typography variant="h4" component="h4">
                    join a Room
                </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Code" value={this.state.roomCode} helperText={this.state.error} variant="outlined" onChange={this.handleFields} />
                </Grid>

                <Grid item xs={12} align="center">
                    <button variant="contained" color="primary" to="/" onClick={this.BtnPressed}> enter Room</button>
                </Grid>
                <Grid item xs={12} align="center">
                    <button variant="contained" color="secondary" to="/" component={Link}> Back</button>
                </Grid>

            </Grid>

        )
    }
    handleFields(e){
        this.setState({
            roomCode : e.target.value
        })
    }
    BtnPressed(){
        const requestOptions = {
            method :"POST",
            headers : {"Content-Type" : "application/json"},
            body : JSON.stringify({
                code: this.state.roomCode
            })
        }
        fetch('/api/join-room', requestOptions).then((response) => console.log(response))
    }
}

export default JoinPage
