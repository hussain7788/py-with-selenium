import React from "react";
import { MouseEvent } from "react";

function ListGroup() {
  const items = ["India", "USA", "London", "China", "Korea"];
  const [click, setClick] = React.useState(false)
  const [index, setIndex] = React.useState(0)


  // ternary opertor is used to write logic
  // {items.length == 0 ? <p>No items</p> : <p>do </p>}
  const ms = items.length == 0 ? <p>no items</p> : <p>do something</p>;
  const getMessage = () => {
    if (items.length == 0) {
      return <p>no items</p>;
    } else {
      return <p>so something</p>;
    }
  };
//   function handleClick(e: MouseEvent) {
    
//   }

  return (
    <>
      <h3>List Group</h3>

      <ul className="list-group">
        {items.map((item, i) => {
          return (
            <li key={item} className={index == i ? 'list-group-item active': 'list-group-item'} onClick={() => setIndex(i)}>
              {item}
            </li>
          );
        })}
      </ul>
    </>
  );
}

export default ListGroup;
