import React, { Component } from 'react'

class Class_Array extends Component {

    MyElement(names) {
        return names.map(name =>
            <div>
                {`${name}`}
                
            </div>
            )
    }

    render() {
        return (
            <div>
                <h2> {this.MyElement(this.props.names)}</h2>
            </div>
        )
    }
}

export default Class_Array
