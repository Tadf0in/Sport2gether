import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import { client } from '../App';
import { Loading } from './questionnaire/Fields';


function Userview() {
    const navigate = useNavigate()
    const [userData, setUserData] = useState({})

    useEffect(() => {
        const getUserData = async () => {
            await client.get("/api/user")
            .then((res) => {
                setUserData(res.data.user)
            })
            .catch((err) => {
                navigate('/login')
            });
        } 
        getUserData()
    }, []);

    if (Object.keys(userData).length === 0) {
        return <Loading />
    } else {
        console.log(userData)
        return (
            <div>
            <h1>Bonjour, {userData.first_name}</h1>
                <button onClick={() => navigate('/login')} className='btn btn-danger' type='button'>Déconnexion</button>
            </div>
        )
    }
}

export default Userview