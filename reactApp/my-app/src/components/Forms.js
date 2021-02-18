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

    }
    passwordHandler = (event) => {
        this.setState({
            password:event.target.value
        })

    }


    render() {
        return (
            <div className='container'>
                <input type='text' value={this.state.user_name} placeholder="enter username" className='form-control' onChange={this.usernameHandler}/>
                <input type='text' value={this.state.password} placeholder="enter password" className='form-control'onChange={this.passwordHandler}/>
                <button className='btn btn-primary'>Button</button>

            </div>
        )
    }
}

export default Forms;
