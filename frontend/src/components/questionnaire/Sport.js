import React from 'react'

function Sport() {
  return (
    <div className='questionnaire-sport form-body'>
        <span className='span-sports'>
            <span className='span-sport'>
                <input type='checkbox' id="velo"/>
                <label htmlFor='velo'>Vélo</label>
            </span>
            <span className='span-sport'>
                <input type='checkbox' id="nage"/>
                <label htmlFor='nage'>Natation</label>
            </span>
            <span className='span-sport'>
                <input type='checkbox' id="cap"/>
                <label htmlFor='cap'>Course à pied</label>
            </span>  
        </span>
        <select name="select-frenquecy">
            <option selected hidden>Fréquence d'entraînement</option>
            <option value="tlj">Tous le jours</option>
            <option value="tet">De temps en temps</option>
            <option value="var">Variable</option>
        </select>
        <input type='text' name='ville' placeholder='Adresse ou ville'/>
    </div>
  )
}

export default Sport