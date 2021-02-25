import React, {Component} from 'react';

class Name extends Component{
    constructor(){
        super()
        this.state={
            name:'hussain',
            age:23,
            email:'email.com'
        }
    } 
    ClickMe= () => {
        if(this.state.name == "hussain"){
            this.setState({
                name : "valli"
            })
        }
        else{
            this.setState({
                name : "hussain"
            })
        }
    }

    render(){
        return(
            <div>
            <p>{this.state.name} : this is name component</p>
            <button className='btn btn-primary' onClick={this.ClickMe}>name button</button>
            </div>
        )
    }
}

export default Name;