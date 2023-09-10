import React, {useState, useEffect} from 'react'
import Input, {Loading} from './Fields'
import { client } from '../../App'
const sportValidation = (formData) => {
    if (formData.frequence !== '') {
        if (formData.ville !== '') {
            return 'OK'
        }
    }
}

function Sport({ formData, setFormData }) {
    const [sports, setSports] = useState([])

    useEffect(() => {
        const getSportsApi = async () => {
            await client.get('/api/sports')
            .then((res) => {
                setSports(res.data)
            }) 
            .catch(err => console.log(err))
        }
        getSportsApi()
    }, [])

    const SpanSport = ({sport, checked}) => {
        if (sports.length === 0) {
            return <Loading />
        } else {
            return (
                <div className="form-check">
                    <input className="form-check-input" type="checkbox" value={sport.abrev} id={sport.id} 
                    checked={checked} onKeyDown={e => e.preventDefault()} 
                    onChange={(event) => {
                        setFormData({
                            ...formData, sports: {
                                ...formData.sports, [sport.abrev]: event.target.checked
                            }
                        })
                    }}
                />
                    <label className="form-check-label" htmlFor={sport.id}>
                        {sport.name}
                    </label>
                </div>
            )
        }
    }
    const SpanSports = ({sports}) => {
        return (
            <div className='span-sports'>{
                Object.keys(sports).map((sport, i) => {
                    return (
                        <SpanSport sport={sports[sport]} key={i} checked={formData.sports[[sports[sport].abrev]]} />
                    )
                })}    
            </div>
        )
    }

    const initChecks = () => {
        let getcheck = {}
        for (let sport of sports) {
            getcheck[sport['abrev']] = false
        }
        setFormData({...formData, sports: getcheck})
    }

    if (sports.length === 0) { 
        return <Loading />
    } else {
        if (Object.keys(formData.sports).length === 0) {
            initChecks()
        }
        
        return (
            <div className='form-body'>
                <SpanSports sports={sports}/>
                <select name="select-frequency" className='form-select'
                value={formData.frequence} 
                onChange={(event) => setFormData({...formData, frequence: event.target.value})}>
                    <option defaultValue={true} hidden>Fréquence d'entraînement</option>
                    <option value="tlj">Tous le jours</option>
                    <option value="tet">De temps en temps</option>
                    <option value="var">Variable</option>
                </select>
                
                <Input type='text' placeholder='Adresse ou ville' dataName='ville'
                formData={formData} setFormData={setFormData}>Ville :</Input>
            </div>
        )
    }
}

export default Sport
export {sportValidation}