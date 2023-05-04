import React from 'react'

function Messages() {
    const name:String = '';
     if(name) {
        return <div>hello {name}</div>
     }
     
    return (
        <div>hello</div>
    )
        
 
}

export default Messages