import { useState } from 'react'
import Header from './Component/Header'
import MainPage from './Component/MainPage'
import "./App.css";

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
    <div className='Header'>
    <Header></Header>
    </div>

    <div className='obs'></div>
    
    
    <div className='Main'>
      <MainPage></MainPage>
    </div>
    

    </div>
  )
}
export default App
