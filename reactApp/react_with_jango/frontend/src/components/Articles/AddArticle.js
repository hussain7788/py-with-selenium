import React, { Component } from 'react';
import {TextField, Button, Grid, Typography} from "@material-ui/core";
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";
import axios from 'axios';
const api = axios.create({
    baseURL: "http://localhost:3000/contacts/"
})

export class AddArticle extends Component {
        constructor(props) {
            super(props)
        
            this.state = {
                id : '',
                name : '',
                email : '',
                age : '',
                 
            }
            this.changeHandler = this.changeHandler.bind(this);
            this.submitForm = this.submitForm.bind(this);

        }
        
    // input change handler
    changeHandler(event){
        this.setState({
            [event.target.name]:event.target.value
        });
    }

    // submit form
    submitForm= async(e) => {
        e.preventDefault();
        try{
            let res = await api.post('/', this.state)
            console.log("post data", res.data)
     // this is function we got from parent and sending data from child to parent
            this.props.sample(this.state);
     // this is after adding data to server fields gets clear
            this.setState({
                id:"",
                name:"",
                email:"",
                age:""
            })

        }catch(error){
            console.log(error)
        }
    }


        // const request = new Request(
        //     'http://127.0.0.1:8000/api/api_article/',
        //     {headers: {'X-CSRFToken': csrftoken}}
        // );
        // fetch(request, {
        //     method: 'POST',
        //     mode: 'same-origin'  // Do not send CSRF token to another domain.
        // })
        // .then(response => response.json())
        // .then(data => console.log("post data is", data))

// another method 

        // fetch('http://127.0.0.1:8000/api/api_article/',{
        //     method:'POST',
        //     body:JSON.stringify(this.state),
        //     headers:{
        //         'Content-type': 'application/json; charset=UTF-8',
        //     },
        // })
        // .then(response=>response.json())
        // .then((data)=>console.log("post data is", data));

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                <Typography variant="h4" component="h4">
                    Add Article
                </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Id" name="id" value={this.state.id} onChange={this.changeHandler} variant="outlined" />
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Name" name="name" value={this.state.name} onChange={this.changeHandler} variant="outlined" />
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Email" name="email" value={this.state.email} onChange={this.changeHandler}  variant="outlined" />
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Age" name="age" value={this.state.age} onChange={this.changeHandler}  variant="outlined" />
                </Grid>

                <Grid item xs={12} align="center">
                    <button className="btn btn-primary" onClick={this.submitForm}>Add</button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Link to="/">
                    <button className="btn btn-secondary" > Back</button>
                    </Link>
                </Grid>

            </Grid>
        )
    }
}

export default AddArticle;
