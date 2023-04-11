import React, { useEffect ,useState} from "react";
import Popup from "reactjs-popup";
import axios, { Axios } from "axios";



function Results(){

  const displayresults = () =>{
    axios.get("http://127.0.0.1:5000/results")
    .then(res=>{
      console.log(res)

    }).catch(err=>{
      console.log(err)
    })

  }

return(

  <div>
  

<div className="d-grid gap-2 button">
     <button className="btn btn-primary " type="button" onClick={displayresults} >Submit</button>

  
  
  
  </div>

  </div>
)
}export default Results