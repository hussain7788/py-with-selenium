import React from 'react'
import './App.css'
import Messages from './components/messages'
import ListGroup from './components/ListGroup'
import Props from './components/Props'
import Alert from './components/Alert'
import Button from './components/Button'

function App() {

  const items = ["India", "USA", "London", "China", "Korea"];
  
  // passing this function to children and getting selected item of children
  const handleSelectItem = (item: string) => {
      console.log(item)
  }

  return (
    <div>
      {/* <ListGroup /> */}
      {/* <Props items={items} heading='List Group' onSelectItem={handleSelectItem} /> */}
      {/* <Alert>
        Hello world
        <br />
        <span>this is span tag</span>
      </Alert> */}
      <Button></Button>

    </div>
      
  )
}

export default App
