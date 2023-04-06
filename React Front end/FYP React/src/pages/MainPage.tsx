import "./MainPage.css"
import "../App.css"
import Modal from '../button/Modal'
import React, { useState } from 'react';
import axios from "axios";



function MainPage(){


  const [openModal, setOpenModal] = useState(false);
  const [Val, setVal] = useState("")
  var namee="";
  var twitterr=""


  const SendData = ()=>{


    axios.post("http://127.0.0.1:5000/home",
    {
      "name":namee,
      "twitter":twitterr
    },{headers:{"Access-Control-Allow-Origin": "*"}});
    
    
  }


  const Onchange = (event: React.ChangeEvent<HTMLInputElement>) =>{
    namee=(event.target.value)
  }

  const Onchange1 = (event: React.ChangeEvent<HTMLInputElement>) =>{
    twitterr=(event.target.value)
  }


    return(
    
        <form className="form" >

        <div className="bar2"></div>   

        <div className="form">

        <div className="row mb-3">
          <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Name</label>
          <div className="col-sm-10">
            <input type="text" className="form-control" id="inputEmail3" onChange={Onchange} ></input>
          </div>
        </div>

        <div className="row mb-3 ">
          <label htmlFor="inputPassword3" className="col-sm-2 col-form-label">twitter </label>
          <div className="col-sm-10">
            <input type="text" className="form-control" id="inputPassword3" onChange={Onchange1}></input>
          </div>
        </div>

        </div>

     <div className="d-grid gap-2 button">
     <button className="btn btn-primary " type="button" onClick={() => {SendData(); setOpenModal(true) }} >Submit</button>
     <Modal 
      open={openModal} 
      onClose={() => setOpenModal(false)} />
     
    </div>

    <div className="bar1"></div>  

      </form>
      
      
    )
}export default MainPage