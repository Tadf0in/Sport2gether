import React from 'react'

function Objectifs() {
  return (
    <div className='questionnaire-objectifs form-body'>
        <input type='text' name='obj-court' placeholder='Objectifs à court terme'/>
        <input type='text' name='obj-long' placeholder='Objectifs à long terme'/>
        <input type='text' name='defi' placeholder='Plus grand défi réalisé'/>
    </div>
  )
}

export default Objectifs