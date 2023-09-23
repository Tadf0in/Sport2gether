import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import Register, {registerValidation} from './Register'
import Infos, {infosValidation} from './Infos'
import Sport, {sportValidation} from './Sport'
import Objectifs from './Objectifs'
import Questions from './Questions'
import { client } from '../../App'


function Form() {
    const navigate = useNavigate()
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
        sports: {},
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

    useEffect(() => {
        const logout = async () => {
            await client.post('/api/user/logout')
            .catch((err) => console.log(err))
        }
        logout()
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
            return (
                <div className="alert alert-danger" role="alert">
                    {alert}
                </div>
            )
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

    const submitRegistration = async (e) => {
        e.preventDefault()

        await client.post("/api/user/register", formData)
        .then((res) => {
            navigate('/login')
        })
        .catch((err) => {
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

                    <br />
                    <a href='/login' hidden={page > 0}>J'ai déjà un compte</a>
                </div>
            </form>            
        </div>
    )
}

export default Form