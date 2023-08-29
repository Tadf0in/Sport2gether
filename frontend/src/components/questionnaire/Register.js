import React from 'react'
import Input from './Fields'

const registerValidation = (formData) => {
  if (formData.password === formData.confirm_pass) {
    const email_pattern = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    const pass_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/
    if (email_pattern.test(formData.email)) {
      if (pass_pattern.test(formData.password)) {
        return true
      } else {
        // throw new Error("Le mot de passe est trop faible")
        return false
      }
    } else {
      // throw new Error("L'adresse mail est invalide")
      return false
    }
  } else {
    // throw new Error("Les mots de passe ne correspondent pas")
    return false
  }
}

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
export {registerValidation}