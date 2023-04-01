import "./MainPage.css"

function MainPage(){
    return(
        
        <form className="form" >

        <div className="bar2"></div>   

        <div className="form">

        <div className="row mb-3">
          <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">Name</label>
          <div className="col-sm-10">
            <input type="email" className="form-control" id="inputEmail3"></input>
          </div>
        </div>

        <div className="row mb-3 ">
          <label htmlFor="inputPassword3" className="col-sm-2 col-form-label">twitter </label>
          <div className="col-sm-10">
            <input type="password" className="form-control" id="inputPassword3"></input>
          </div>
        </div>

        </div>

     <div className="d-grid gap-2 button">
     <button className="btn btn-primary" type="button">Submit</button>
     
    </div>

    <div className="bar1"></div>  

      </form>
      
      
    )
}export default MainPage