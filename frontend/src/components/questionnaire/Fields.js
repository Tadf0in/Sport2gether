import React from 'react'

function Input({ type, placeholder, dataName, error='', children, formData, setFormData}) {

  const preventSubmit = (e) => {
    if (e.keyCode === 13 || e.key === 'Enter') {
      e.preventDefault()
    }
  } 

  return (
    <div className="form-floating mb-3">
        <input type={type} placeholder={placeholder} value={formData[dataName]} onKeyDown={preventSubmit}
        className='form-control textinput' id={dataName + 'forminput'} style={error.style}
        onChange={(event) => setFormData({...formData, [dataName]: event.target.value})}/>
        <label htmlFor={dataName + 'forminput'} className="form-label">{children}</label>
        <span className="field-error">{error.message}</span>
    </div>
  )
}

export default Input;

function Textarea({ dataName, children, formData, setFormData }) {
  return (
    <div className="mb-3">
        <label htmlFor={dataName + 'textarea'} className="form-label">{children}</label>
        <textarea className="form-control" id={dataName + 'textarea'} rows="3"
        value={formData[dataName]} 
        onChange={(event) => setFormData({...formData, [dataName]: event.target.value})}>
        </textarea>
    </div>
  )
}

export {Textarea}


function Loading() {
  return (
    <div className="spinner-grow text-secondary" role="status">
      <span className="visually-hidden">Loading...</span>
    </div>
  )
}

export {Loading}