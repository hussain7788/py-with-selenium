import React from 'react'

interface Props {
    children: string;
    onClick: () => void;
}
export default function Button() {
    const [btn, setBtn] = React.useState(true)

    function handleClickBtn(){
        console.log('clicked')
        return btn ? setBtn(false) : setBtn(true)
    }
  return (
    <div>
        <button type='button' className={btn ? 'btn btn-primary': 'btn btn-danger'} onClick={() => handleClickBtn()} >My Button</button>
    </div>
  )
}
