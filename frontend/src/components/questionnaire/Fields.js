import React from 'react'

function Input({ type, placeholder, dataName, children, formData, setFormData}) {
  return (
    <div className="form-floating mb-3">
        <input type={type} placeholder={placeholder} value={formData[dataName]} 
        className='form-control' id={dataName + 'forminput'}
        onChange={(event) => setFormData({...formData, [dataName]: event.target.value})}/>
        <label htmlFor={dataName + 'forminput'} className="form-label">{children}</label>
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