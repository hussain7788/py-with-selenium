import React from 'react'

function Func(props) {
    function ClickMe() {
        alert("this is functional click button")
        
    }
    return (
        <div>
        <h2>my name is: {props.name} and i am legend</h2>
        <button onClick={ClickMe} type="button" className='btn btn-primary'>click me</button>

        </div>
    )
}

export default Func;