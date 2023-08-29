import React from 'react'
import { Textarea } from './Fields'

function Questions({ formData, setFormData }) {
  return (
    <div className='form-body'>
        <label>Comment avez vous trouver l'appli</label>
        <select name="select-raison"  className='form-select'
        value={formData.raison} 
        onChange={(event) => setFormData({...formData, raison: event.target.value})}>
            <option value="ami">Un ami m'en a parlé</option>
            <option value="pub">Une publicité</option>
            <option value="app">Depuis le Play Store</option>
            <option value="oth">...</option>
        </select>
        <Textarea dataName='det_raison' formData={formData} setFormData={setFormData}>Plus de détails :</Textarea>

        <label>Qu'attendez vous de l'appli</label>
        <select name="select-raison" className='form-select' 
        value={formData.attente} 
        onChange={(event) => setFormData({...formData, attente: event.target.value})}>
            <option value="ren">Faire des rencontres</option>
            <option value="mot">Trouver de la motivation</option>
            <option value="oth">...</option>
        </select>
        <Textarea dataName='det_attentes' formData={formData} setFormData={setFormData}>Plus de détails :</Textarea>
    </div>
  )
}

export default Questions