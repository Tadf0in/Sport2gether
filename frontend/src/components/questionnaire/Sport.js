import React from 'react'
import Input from './Fields'

function Sport({ formData, setFormData }) { 

    const SpanSport = ({ abrev, complet, isChecked }) => {
        return (
            // <span className='span-sport'>
            //     <input type='checkbox' id={abrev} checked={isChecked} 
            //     onChange={(event) => {setFormData({
            //         ...formData, sports: {
            //             ...formData.sports, [abrev]: {
            //                 abrev: abrev,
            //                 name: complet,
            //                 checked: event.target.checked
            //             }
            //         }
            //     })}}/>
            //     <label htmlFor={abrev}>{complet}</label>
            // </span>

            <div class="form-check">
                <input class="form-check-input" type="checkbox" value={complet} id={abrev} checked={isChecked}
                onChange={(event) => {
                    setFormData({
                    ...formData, sports: {
                        ...formData.sports, [abrev]: {
                            abrev: abrev,
                            name: complet,
                            checked: event.target.checked
                        }
                    }
                })}}/>
                <label class="form-check-label" htmlFor={abrev}>
                    {complet}
                </label>
            </div>

        )
    }
    const SpanSports = ({sports}) => {
        return (
            <div className='span-sports'>{
                Object.keys(sports).map((sport, i) => {
                    return (
                        <SpanSport abrev={sport} key={i} complet={sports[sport].name} isChecked={sports[sport].checked} />
                    )
                })}    
            </div>
        )
    }

    return (
        <div className='form-body'>
            <SpanSports sports={formData.sports}/>
            <select name="select-frenquecy" className='form-select'
            value={formData.frequence} 
            onChange={(event) => setFormData({...formData, frequence: event.target.value})}>
                <option defaultValue={true} hidden>Fréquence d'entraînement</option>
                <option value="tlj">Tous le jours</option>
                <option value="tet">De temps en temps</option>
                <option value="var">Variable</option>
            </select>
            <Input type='text' placeholder='Adresse ou ville' dataName='ville' formData={formData} setFormData={setFormData}>Ville :</Input>
        </div>
    )
}

export default Sport