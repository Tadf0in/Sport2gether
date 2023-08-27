import React from 'react'

function Sport({ formData, setFormData }) {

    const getCheckedSports = () => {
        let sports_list = []

        for (let [key, value] of Object.entries(formData.sports)) {
            if (value[1] === true) {
                sports_list.push(key)
            }
        }
        return sports_list
    }

    const SpanSport = ({ abrev, complet }) => {
        return (
            <span className='span-sport'>
                <input type='checkbox' id={abrev} checked={getCheckedSports().includes(abrev)} 
                onChange={(event) => {setFormData({...formData, sports: {...formData.sports, [abrev]: [complet, event.target.checked]}})}}/>
                <label htmlFor={abrev}>{complet}</label>
            </span>
            /* exemple (abrev='velo', complet="Vélo") : <input type='checkbox' id="velo" checked={getCheckedSports().includes('velo')} 
            onChange={(event) => {setFormData({...formData, sports: {...formData.sports, velo: ["Vélo", event.target.checked]}})}}/>
            <label htmlFor='velo'>Vélo</label> */
        )
    }
    const SpanSports = ({sports}) => {
        return (
            <div className='span-sports'>{
                Object.keys(sports).map((sport, i) => {
                    return (
                        <SpanSport abrev={sport} complet={sports[sport][0]} />
                    )
                })}    
            </div>
        )
    }

    return (
        <div className='questionnaire-sport form-body'>
            <SpanSports sports={formData.sports}/>
            <select name="select-frenquecy">
                <option defaultValue={true} hidden>Fréquence d'entraînement</option>
                <option value="tlj">Tous le jours</option>
                <option value="tet">De temps en temps</option>
                <option value="var">Variable</option>
            </select>
            <input type='text' name='ville' placeholder='Adresse ou ville' value={formData.ville} onChange={(event) => setFormData({...formData, ville: event.target.value})}/>
        </div>
    )
}

export default Sport