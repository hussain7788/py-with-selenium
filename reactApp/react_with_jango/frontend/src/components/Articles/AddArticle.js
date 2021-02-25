import React, { Component } from 'react';
import {TextField, Button, Grid, Typography} from "@material-ui/core";
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";


export class AddArticle extends Component {
        constructor(props) {
            super(props)
        
            this.state = {
                title : '',
                author : '',
                email : '',
                date : '',
                 
            }
            this.changeHandler = this.changeHandler.bind(this);
            this.submitForm = this.submitForm.bind(this);

        }
        
    // input change handler
    changeHandler(event){
        this.setState({
            [event.target.name]:event.target.value
        });
        console.log(this.state);
    }

    // submit form
    submitForm(){

        const request = new Request(
            'http://127.0.0.1:8000/api/view_article/',
            {headers: {'X-CSRFToken': csrftoken}}
        );
        fetch(request, {
            method: 'POST',
            mode: 'same-origin'  // Do not send CSRF token to another domain.
        })
        .then(response => response.json())
        .then(data => console.log("post data is", data))


        // fetch('http://127.0.0.1:8000/api/view_article/',{
        //     method:'POST',
        //     body:JSON.stringify(this.state),
        //     headers:{
        //         'Content-type': 'application/json; charset=UTF-8',
        //     },
        // })
        // .then(response=>response.json())
        // .then((data)=>console.log("post data is", data));
    }


    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                <Typography variant="h4" component="h4">
                    Add Article
                </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Title" name="title" value={this.state.title} onChange={this.changeHandler} variant="outlined" />
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Author" name="author" value={this.state.author} onChange={this.changeHandler}  variant="outlined" />
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField  error="error" label="Email" name="email" value={this.state.email} onChange={this.changeHandler}  variant="outlined" />
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
