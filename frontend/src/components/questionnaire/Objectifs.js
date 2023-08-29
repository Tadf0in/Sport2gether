import React from 'react'
import Input from './Fields'

function Objectifs({ formData, setFormData }) {
  return (
    <div className='form-body'>
      <Input type='text' placeholder='' dataName='obj_court' formData={formData} setFormData={setFormData}>Objectifs à court terme :</Input>
      <Input type='text' placeholder='' dataName='obj_long' formData={formData} setFormData={setFormData}>Objectifs à long terme :</Input>
      <Input type='text' placeholder='' dataName='defi' formData={formData} setFormData={setFormData}>Plus grand défi réalisé :</Input>
    </div>
  )
}

export default Objectifs