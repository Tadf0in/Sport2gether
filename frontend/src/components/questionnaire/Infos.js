import React from 'react'

function Infos({ formData, setFormData }) {
  return (
    <div className='questionnaire-infos form-body'>
        <input type='text' placeholder='Prénom' value={formData.first_name} onChange={(event) => setFormData({...formData, first_name: event.target.value})}/>
        <input type='text' placeholder='Nom' value={formData.last_name} onChange={(event) => setFormData({...formData, last_name: event.target.value})}/>
        <input type='number' placeholder='Âge' value={formData.age} onChange={(event) => setFormData({...formData, age: event.target.value})}/>
        <span className='span-gender'>
            <label htmlFor='male'>Homme</label>
             <input name='gender' id='male' type='radio' checked={formData.gender === 'H'} value={formData.gender} 
             onChange={() => setFormData({...formData, gender: (formData.gender === 'H' ? 'F' : 'H')})}/>
            <label htmlFor='female'>Femme</label>
            <input name='gender' id='female' type='radio' checked={formData.gender === 'F'} 
            onChange={() => setFormData({...formData, gender: (formData.gender === 'F' ? 'H' : 'F')})}/> 
        </span>
    </div>
  )
}

export default Infos