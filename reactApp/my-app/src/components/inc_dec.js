import React, { Component } from 'react'

export class Inc_dec extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             age : 0,
             number : 1,
        }
    }
    
    Increment = () => {
            this.setState({
                age : this.state.age +++ this.state.number
            })
            console.log(this.state.age)
    }

    Decrement = () => {
        if(this.state.age != 0){
            this.setState({
                age : this.state.age --- this.state.number
            })
        }
        else{
            console.log("zero")
        }
    }

    Handler = (event) => {
        this.setState({
            age : event.target.value
        })
    }

    render() {
        return (
            <div>
                <input type="text" placeholder="age" value={this.state.age} onChange={this.Handler}/>
                <button type="button" onClick={this.Increment}>increase</button>
                <button type="button" onClick={this.Decrement}>decrease</button>

                
            </div>
        )
    }
}

export default Inc_dec
