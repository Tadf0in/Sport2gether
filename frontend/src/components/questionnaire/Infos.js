import React from 'react'

function Infos() {
  return (
    <div className='questionnaire-infos form-body'>
        <input type='text' placeholder='Prénom'/>
        <input type='text' placeholder='Nom'/>
        <input type='number' placeholder='Âge'/>
        <span className='span-gender'>
            <label htmlFor='male'>Homme</label>
            <input name='gender' id='male' type='radio'/>
            <label htmlFor='female'>Femme</label>
            <input name='gender' id='female' type='radio' defaultValue={false}/>
        </span>
    </div>
  )
}

export default Infos