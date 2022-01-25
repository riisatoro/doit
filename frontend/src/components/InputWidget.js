import React from "react";

function InputWidget({name, type, handleChange, value, error}) {
    return (
      <div className='form-group my-2'>
          <input 
            type={type} 
            name={name}
            className="form-control" 
            placeholder={name}
            onChange={handleChange}
            value={value}
          />
          <small className="badge font-weight-bold bg-danger">{error}</small>
        </div>
    )
}

export default InputWidget;
