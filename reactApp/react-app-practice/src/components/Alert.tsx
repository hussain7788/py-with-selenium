import React from 'react'


interface Props {
    children: React.ReactNode
}
export default function Alert({children}:Props) {

  return (
    <div>
        <h4 className='alert alert-primary'>{children}</h4>
    </div>
  )
}
