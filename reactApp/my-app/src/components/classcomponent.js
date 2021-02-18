import React, { Component } from 'react';


class MyClass extends Component{

    ClassClick(){
        alert('this is class component click')
    }

    Button(){
        return(
            <button className='btr btr-primary'>button func</button>
        )
    }
    render(){
        return (
           <div>
            <h1 className='bg-primary-text-white text-center'>my email is: {this.props.my_emai}</h1>
            <button onClick={this.props.myclick} type='button' className='btn btn-secondary'>class button</button>
            <small className='btn btn-primary'> <this.Button/> </small>
           </div>
            
        )
    }

}

export default MyClass;

