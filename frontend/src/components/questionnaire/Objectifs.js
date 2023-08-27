import React from 'react'

function Objectifs({ formData, setFormData }) {
  return (
    <div className='questionnaire-objectifs form-body'>
        <input type='text' name='obj-court' placeholder='Objectifs à court terme' value={formData.obj_court} onChange={(event) => setFormData({...formData, obj_court: event.target.value})}/>
        <input type='text' name='obj-long' placeholder='Objectifs à long terme' value={formData.obj_long} onChange={(event) => setFormData({...formData, obj_long: event.target.value})}/>
        <input type='text' name='defi' placeholder='Plus grand défi réalisé' value={formData.defi} onChange={(event) => setFormData({...formData, defi: event.target.value})}/>
    </div>
  )
}

export default Objectifs