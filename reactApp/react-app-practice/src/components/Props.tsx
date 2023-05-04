import React from 'react'

interface Properties {
    items: string[]
    heading: string;
    // This function commign from parent and getting selected item of children
    onSelectItem: (item: string) => void
}

const  Props = ( {items, heading, onSelectItem}: Properties) => {
    return (
        <>
          <h3>{heading}</h3>
    
          <ul className="list-group">
            {items.map((item, i) => {
              return (
                <li key={item} className='list-group-item' onClick={() => onSelectItem(item)}>
                  {item}
                </li>
              );
            })}
          </ul>
        </>
      );
}

export default Props