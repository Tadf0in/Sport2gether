import React from 'react'

function Questions({ formData, setFormData }) {
  return (
    <div className='questionnaire-questions form-body'>
        <label>Comment avez vous trouver l'appli</label>
        <select name="select-raison" value={formData.raison} onChange={(event) => setFormData({...formData, raison: event.target.value})}>
            <option value="ami">Un ami m'en a parlé</option>
            <option value="pub">Une publicité</option>
            <option value="app">Depuis le Play Store</option>
            <option value="oth">...</option>
        </select>
        <textarea placeholder="Plus de détails" value={formData.det_raison} onChange={(event) => setFormData({...formData, det_raison: event.target.value})}></textarea>

        <label>Qu'attendez vous de l'appli</label>
        <select name="select-raison" value={formData.attente} onChange={(event) => setFormData({...formData, attente: event.target.value})}>
            <option value="ren">Des rencontres</option>
            <option value="mot">Motivation</option>
            <option value="oth">...</option>
        </select>
        <textarea placeholder="Plus de détails" value={formData.det_attentes} onChange={(event) => setFormData({...formData, det_attentes: event.target.value})}></textarea>
    </div>
  )
}

export default Questions