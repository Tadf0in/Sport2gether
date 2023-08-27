import React, { useState } from 'react'
import Register from './Register'
import Infos from './Infos'
import Sport from './Sport'
import Objectifs from './Objectifs'
import Questions from './Questions'


function Form() {

    const [page, setPage] = useState(0)
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        confirm_pass: '',
        first_name: '',
        last_name: '',
        age: '',
        gender: '',
        sports: {
            'velo': ["Vélo", true],
            'nage': ["Natation", false],
            'cap': ["Course à pied", false]
        },
        frequence: '',
        ville: '',
        obj_court: '',
        obj_long: '',
        defi: '',
        raison: '',
        det_raison: '',
        attent: '',
        det_attentes: ''
    })

    const Titles = ["Créez votre compte", "Informations personnelles", "Pratique sportive", "Objectifs", "Questionnaire"]
    const Desc = [
        " ", 
        "Qui êtes vous ?", 
        "Nous vous mettrons en relation avec des personnes qui pratiquent le même sport que vous", 
        "Dites nous en plus sur ce que vous recherchez", 
        "Votre retour est précieux, nous avons besoin de vous pour améliorer l'application"
    ]

    const pageDisplay = () =>  {
        switch (page) {
            case 0:
                return <Register formData={formData} setFormData={setFormData}/>
                break
            case 1:
                return <Infos formData={formData} setFormData={setFormData}/>
                break
            case 2:
                return <Sport formData={formData} setFormData={setFormData}/>
                break
            case 3:
                return <Objectifs formData={formData} setFormData={setFormData}/>
                break
            case 4:
                return <Questions formData={formData} setFormData={setFormData}/>
                break
            default:
                throw new Error('Page de questionnaire inconnue')
        }
    }

    const skipDisplay = () => {
        if (page > 2){                        
            return <button className='skip'>SKIP</button>
        }
    }

    return (
        <div className='form'>
            <div className='progressbar'>
                <div className='progress' style={{width: 100*page/(Titles.length-1) + "%"}}>&nbsp;</div>
            </div>
            <div className='form-container'>
                <div className='header'>
                    <span>
                        <h1>{Titles[page]}</h1>
                        {skipDisplay()}
                    </span>
                    <h4>{Desc[page]}</h4>
                </div>

                <div className='body'>
                    {pageDisplay()}
                </div>

                <div className='footer'>
                    <button 
                    disabled={page===0}
                    onClick={() => setPage(page - 1)}
                    >Précédent</button>
                    <button 
                    disabled={page === Titles.length - 1}
                    onClick={() => setPage(page + 1)}
                    >Suivant</button>
                </div>
            </div>            
        </div>
    )
}

export default Form