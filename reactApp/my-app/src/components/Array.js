import React from 'react'

function MyElement(names) {
    return names.map(name =>
        <div key = {name}>
            {`${name}`}
        </div>
        )
}

function Example(props) {
    return (
        <div>
            <h2>{MyElement(props.names)}</h2>
        </div>
    )
}

export default Array
