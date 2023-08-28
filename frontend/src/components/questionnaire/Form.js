import React, { useState, useEffect } from 'react'
import Register from './Register'
import Infos from './Infos'
import Sport from './Sport'
import Objectifs from './Objectifs'
import Questions from './Questions'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;


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
            return <button type='button' name='register' value='skip' className='skip'
            onClick={() => submitRegistration(formData)}>SKIP</button>
        }
    }

    function submitRegistration(data) {
        // Vérification
        let infos = {
            username: data.email,
            password: data.password,
            sexe:data.gender,
            age: data.age,
            first_name:data.first_name,
            last_name:data.last_name,
            ville:data.ville,
            obj_court: data.obj_court,
            obj_long: data.obj_long,
            defi: data.defi,
            frequence: data.frequence,
        }
        console.log(infos, typeof(infos.age))

        axios.post("http://127.0.0.1:8000/api/register", infos)

        // axios.post("http://127.0.0.1:8000/api/register", to_post, {headers:{"Content-Type" : "application/json"}})
        // .catch((err) => console.log(err))
        // // ).then(function(res) {
        //   axios.post(
        //     "/api/login",
        //     {
        //       username: data.email,
        //       password: data.password
        //     }
        //   ).then(function(res) {
        //     setCurrentUser(true);
        //   });
        // });
        // console.log(data, to_post)
    }

    return (
        <div className='form'>
            <div className='progressbar'>
                <div className='progress' style={{width: 100*page/(Titles.length-1) + "%"}}>&nbsp;</div>
            </div>
            <form className='form-container'>
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
                    <button className='previous' name='register' value='previous' type='button'
                    disabled={page===0}
                    onClick={() => setPage(page - 1)}
                    >Précédent</button>
                    <button className='next' name='register' value='finish' type='button'
                    onClick={() => {
                        if (page === (Titles.length - 1)) {
                            submitRegistration(formData)
                        } else {
                            setPage(page + 1)
                        }
                    }}>
                    {page === (Titles.length - 1) ? "Terminer" : "Suivant"}
                    </button>
                </div>
            </form>            
        </div>
    )
}

export default Form