import React from 'react'

function Register({ formData, setFormData }) {
  return (
    <div className='questionnaire-register form-body'>
        <input type='email' placeholder='Adresse mail' value={formData.email} onChange={(event) => setFormData({...formData, email: event.target.value})}/>
        <input type='password' placeholder='Mot de passe' value={formData.password} onChange={(event) => setFormData({...formData, password: event.target.value})}/>
        <input type='password' placeholder='Répétez le mot de passe' value={formData.confirm_pass} onChange={(event) => setFormData({...formData, confirm_pass: event.target.value})}/>
    </div>
  )
}

export default Register