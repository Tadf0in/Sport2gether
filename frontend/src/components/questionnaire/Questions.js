import React from 'react'

function Questions({ formData, setFormData }) {
  return (
    <div className='questionnaire-questions form-body'>
        <label>Comment avez vous trouver l'appli</label>
        <select name="select-raison">
            <option value="friend">Un ami m'en a parlé</option>
            <option value="ad">Une publicité</option>
            <option value="appstore">Depuis le Play Store</option>
            <option value="other">...</option>
        </select>
        <textarea placeholder="Plus de détails" value={formData.det_raison} onChange={(event) => setFormData({...formData, det_raison: event.target.value})}></textarea>

        <label>Qu'attendez vous de l'appli</label>
        <select name="select-raison">
            <option value="meet">Des rencontres</option>
            <option value="shake">Motivation</option>
            <option value="other">...</option>
        </select>
        <textarea placeholder="Plus de détails" value={formData.det_attentes} onChange={(event) => setFormData({...formData, det_attentes: event.target.value})}></textarea>
    </div>
  )
}

export default Questions