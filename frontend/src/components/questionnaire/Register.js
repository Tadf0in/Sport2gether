import React from 'react'
import Input from './Fields'

function Register({ formData, setFormData }) {
  return (
    <div className='form-body'>
        <Input type='email' placeholder='johndoe@example.com' dataName='email' formData={formData} setFormData={setFormData}>Email :</Input>
        <Input type='password' placeholder='Mot de passe..' dataName='password' formData={formData} setFormData={setFormData}>Mot de passe :</Input>
        <Input type='password' placeholder='Mot de passe..' dataName='confirm_pass' formData={formData} setFormData={setFormData}>Répétez le mot de passe :</Input>
    </div>
  )
}

export default Register