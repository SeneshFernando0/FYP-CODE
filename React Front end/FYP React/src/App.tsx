import { useState } from 'react'
import Header from './Component/Header'
import MainPage from './pages/MainPage'
import "./App.css";
import { Link ,Route,RouterProvider, createBrowserRouter} from 'react-router-dom';
import AboutUs from './pages/AboutUs';
import Results from './pages/Results';


const router = createBrowserRouter([
  {
    path:"/",
    element:  <div className='Main'><MainPage></MainPage></div>
  },

  {
    path:"/aboutus",
    element: <div><AboutUs></AboutUs></div>
  
  },

  {
    path:"/results",
    element: <div><Results></Results></div>
  
  }
]);

function App() {




  const [count, setCount] = useState(0)

  return (
    <div>
    <Header></Header>
    <RouterProvider router={router}/>

    </div>
  )
}
export default App
