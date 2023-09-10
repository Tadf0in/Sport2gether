import React from 'react'
import Input from './Fields'

const registerValidation = (formData) => {

  const email_pattern = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
  const pass_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/

  if (formData.password === formData.confirm_pass) {
  
    if (pass_pattern.test(formData.password)) {
      
      if (email_pattern.test(formData.email)) {
        
        return 'OK'

      } else if (formData.email !== '') {
        return 'mailError'
      }
    
    } else if (formData.password !== '') {
      return 'passError'
    }

  } else if (formData.confirm_pass !== '') {
    return 'confirmError'
  }
}

function Register({ formData, setFormData }) {
  const error = registerValidation(formData)

  return (
    <div className='form-body'>
        <Input type='email' placeholder='johndoe@example.com' dataName='email' 
        error={(error === 'mailError') ? {message: "L'adresse mail est invalide", style:{borderColor: 'red'}} : ''} 
        formData={formData} setFormData={setFormData}>Email :</Input>
        
        <Input type='password' placeholder='Mot de passe..' dataName='password' 
        error={(error === 'passError') ? {message: "Le mot de passe est trop faible", style:{borderColor: 'red'}} : ''} 
        formData={formData} setFormData={setFormData}>Mot de passe :</Input>
        
        <Input type='password' placeholder='Mot de passe..' dataName='confirm_pass' 
        error={(error === 'confirmError') ? {message: "Les mots de passe ne correspondent pas", style:{borderColor: 'red'}} : ''} 
        formData={formData} setFormData={setFormData}>Répétez le mot de passe :</Input>
    </div>
  )
}

export default Register
export {registerValidation}