import React, { Component } from 'react'

class Forms extends Component {
    constructor(props){
        super(props)
        this.state = {
            user_name :'',
            password : '',
        }

    }
    usernameHandler = (event) => {
        this.setState({
            user_name:event.target.value
        })
        console.log("username is", this.state.user_name)        

    }
    passwordHandler = (event) => {
        this.setState({
            password:event.target.value
        })
        console.log("password is", this.state.password)        
    }

    Submit(){
        let u_name = document.getElementById("name").value;
        let p = document.getElementById("password").value;
        console.log(u_name, p)


    }


    render() {
        return (
            <div className='container'>
                <input type='text' value={this.state.user_name} id="name" placeholder="enter username" className='form-control' onChange={this.usernameHandler}/>
                <input type='text' value={this.state.password} id="password" placeholder="enter password" className='form-control'onChange={this.passwordHandler}/>
                <button className='btn btn-primary' onClick={this.Submit}>Button</button>

            </div>
           
        )
    }
}

export default Forms;
