import React, { useState, useEffect } from 'react'
import Register, {registerValidation} from './Register'
import Infos, {infosValidation} from './Infos'
import Sport, {sportValidation} from './Sport'
import Objectifs from './Objectifs'
import Questions from './Questions'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


function Form() {
    const [page, setPage] = useState(0)
    const [alert, setAlert] = useState('')
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirm_pass: '',
        first_name: '',
        last_name: '',
        age: '',
        gender: '',
        sports: [],
        frequence: '',
        ville: '',
        obj_court: '',
        obj_long: '',
        defi: '',
        raison: '',
        det_raison: '',
        attente: '',
        det_attentes: ''
    })

    const setSportsList = (sportsData) => {
        let sportsList = []
        for (let i in sportsData) {
            sportsList[[sportsData[i].abrev]] = {
                name: sportsData[i].name,
                icon_url: sportsData[i].icon_url,
                checked: false,
            } 
        }
        setFormData({...formData, sports: sportsList})
    }   

    useEffect(() => {
        const getSportsApi = async () => {
            await axios.get('http://127.0.0.1:8000/api/sports')
            .then((res) => {
                if (formData.sports.length === 0) {
                    setSportsList(res.data)
                }
            }) 
            .catch(err => console.log(err))
        }
        getSportsApi()
    }, [])

    const Titles = ["Créez votre compte", "Informations personnelles", "Pratique sportive", "Objectifs", "Questionnaire"]
    const Desc = [
        ".", 
        "Qui êtes vous ?", 
        "Nous vous mettrons en relation avec des personnes qui pratiquent le même sport que vous", 
        "Dites nous en plus sur ce que vous recherchez", 
        "Votre retour est précieux, nous avons besoin de vous pour améliorer l'application"
    ]

    const pageDisplay = () =>  {
        switch (page) {
            case 0:
                return <Register formData={formData} setFormData={setFormData}/>
            case 1:
                return <Infos formData={formData} setFormData={setFormData}/>
            case 2:
                return <Sport formData={formData} setFormData={setFormData}/>
            case 3:
                return <Objectifs formData={formData} setFormData={setFormData}/>
            case 4:
                return <Questions formData={formData} setFormData={setFormData}/>
            default:
                throw new Error('Page de questionnaire inconnue')
        }
    }

    const alertDisplay = () => {
        if (alert !== '' && page === 0) {
            return <div class="alert alert-danger" role="alert">
                        {alert}
                    </div>
        }
    }

    useEffect(() => {
        setAlert('')
    }, [formData.email])

    const formPageValidation = () => {
        switch (page) {
            case 0:
                return registerValidation(formData) === 'OK'
            case 1:
                return infosValidation(formData) === 'OK'
            case 2:
                return sportValidation(formData) === 'OK'
            case 3:
                return true
            case 4:
                return true
            default:
                return false
        }
    }

    const submitRegistration = (e) => {
        e.preventDefault()
        console.log(formData)
        axios.post("http://127.0.0.1:8000/api/register", formData)
        .then((res) => {
            console.log(res)
            // redirect login
        })
        .catch((err) => {
            console.log(err)
            if (err.response.status === 500) {
                setAlert("Cette adresse mail est déjà utilisée")
            } else {
                setAlert("Une erreur est survenue, vérifiez vos informations puis réessayez")
            }
            setPage(0)
        })
    }

    return (
        <div className='form' id='form'>
            <div className='progress'>
                <div className='progress-bar'  role="progressbar" style={{width: 100*page/(Titles.length-1) + "%"}}>&nbsp;</div>
            </div>

            <form className='form-container' method='POST' onSubmit={submitRegistration}>
                <div className='form-header'>
                    <span>
                        <h1>{Titles[page]}</h1>
                            <button hidden={page < 3} type='submit' name='register' value='skip' className='btn btn-secondary'>SKIP</button>
                    </span>
                    <h4>{Desc[page]}</h4>
                </div>
                {alertDisplay()}

                {pageDisplay()}
                
                <div className='form-footer'>
                    <button className='btn btn-primary' name='page' value='previous' type='button'
                    hidden={page===0} onClick={() => setPage(page - 1)}>Précédent</button>

                    <button className='btn btn-primary' name='register' value='next' type='button'
                    disabled={!formPageValidation()} onClick={() => setPage(page + 1)} 
                    hidden={page === Titles.length - 1}>Suivant</button>

                    <button className='btn btn-primary' name='page' value='finish' type='submit' 
                    hidden={page !== Titles.length - 1}>Terminer</button>
                </div>
            </form>            
        </div>
    )
}

export default Form