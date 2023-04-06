import React from 'react';
import icon from "../button/icon.jpg"
import "../App.css";
import {Routes, Route, useNavigate} from 'react-router-dom';


const Modal = ({ open, onClose }) => {

  const navigate = useNavigate();

  const toresult = () => {
    
    navigate('/results');
  };


  if (!open) return null;
  return (
    <div onClick={onClose} className='overlay'>
      <div
        onClick={(e) => {
          e.stopPropagation();
        }}
        className='modalContainer'
      >
        <img src={icon} alt='/' />
        <div className='modalRight'>
          <p className='closeBtn' onClick={onClose}>
            X
          </p>
          <div className='content'>
            <p>Generate </p>
            
            <p>Book Recommendations</p>
          </div>
          <div className='btnContainer'>
            <button className='btnPrimary' onClick={toresult}>
              <span className='bold'>YES</span>, Get Results
            </button>
            <button className='btnOutline'>
              <span className='bold'>NO</span>, Try again
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Modal;