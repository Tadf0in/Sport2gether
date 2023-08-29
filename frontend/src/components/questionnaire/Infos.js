import React from 'react'
import Input from './Fields'

function Infos({ formData, setFormData }) {
  return (
    <div className='form-body'>
        <Input type='text' placeholder='John' dataName='first_name' formData={formData} setFormData={setFormData}>Prénom :</Input>
        <Input type='text' placeholder='Doe' dataName='last_name' formData={formData} setFormData={setFormData}>Nom :</Input>
        <Input type='number' placeholder='18' dataName='age' formData={formData} setFormData={setFormData}>Âge :</Input>

        <div className='span-gender'>
          <div className='form-check'>
            <label htmlFor='male' className="form-check-label">Homme</label>
            <input name='gender' id='male' type='radio' className="form-check-input"
            checked={formData.gender === 'H'} value={formData.gender} 
            onChange={() => setFormData({...formData, gender: (formData.gender === 'H' ? 'F' : 'H')})}/>
          </div>      
          <div className='form-check'>
            <label htmlFor='female' className="form-check-label">Femme</label>
            <input name='gender' id='female' type='radio' className="form-check-input"
            checked={formData.gender === 'F'} 
            onChange={() => setFormData({...formData, gender: (formData.gender === 'F' ? 'H' : 'F')})}/> 
          </div>
        </div>
    </div>

    
  )
}

export default Infos