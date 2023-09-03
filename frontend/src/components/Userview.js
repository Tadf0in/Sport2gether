import React, { useState, useEffect, useReducer } from 'react'
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
                console.log(err)
                navigate('/login')
            });
        } 
        getUserData()
    }, []);

    const logout = async (e) => {
        await client.post('/api/logout')
        .then((res) => {
            console.log(res)
            navigate('/login')
        })
        .catch((err) => {
            console.log(err)
        })
    }

    if (Object.keys(userData).length === 0) {
        return <Loading />
    } else {
        console.log(userData)
        return (
            <div>
            <h1>Bonjour, {userData.first_name}</h1>
                <button onClick={logout} className='btn btn-danger' type='button'>Déconnexion</button>
            </div>
        )
    }
}

export default Userview