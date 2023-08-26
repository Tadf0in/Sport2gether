import React from 'react'

function Questions() {
  return (
    <div className='questionnaire-questions form-body'>
        <label>Comment avez vous trouver l'appli</label>
        <select name="select-raison">
            <option value="friend">Un ami m'en a parlé</option>
            <option value="ad">Une publicité</option>
            <option value="appstore">Depuis le Play Store</option>
            <option value="other">...</option>
        </select>
        <label>Qu'attendez vous de l'appli</label>
        <textarea placeholder="Plus de détails"></textarea>

        <select name="select-raison">
            <option value="meet">Des rencontres</option>
            <option value="shake">Motivation</option>
            <option value="other">...</option>
        </select>
        <textarea placeholder="Plus de détails"></textarea>
    </div>
  )
}

export default Questions