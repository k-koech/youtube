import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='bg-red-900 text-white' >

        <h1 className='text-4xl p-6 font-roboto'>HELLO YOUTUBE</h1>
        <h5 className='p-6 text-3xl font-sixtyfour'>Happy new year 2025</h5>

      </div>
    </>
  )
}

export default App
