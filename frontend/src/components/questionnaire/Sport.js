import React from 'react'

function Sport({ formData, setFormData }) { 

    const SpanSport = ({ abrev, complet, isChecked }) => {
        return (
            <span className='span-sport'>
                <input type='checkbox' id={abrev} checked={isChecked} 
                onChange={(event) => {setFormData({
                    ...formData, sports: {
                        ...formData.sports, [abrev]: {
                            abrev: abrev,
                            name: complet,
                            checked: event.target.checked
                        }
                    }
                })}}/>
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
                        <SpanSport abrev={sport} complet={sports[sport].name} isChecked={sports[sport].checked} />
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