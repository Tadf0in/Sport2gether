import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import { client } from '../App';


function Userview() {
    const navigate = useNavigate()

    const logout = async (e) => {
        await client.post('/api/logout')
        .then((res) => {
            console.log(res)
            // navigate('/')
        })
        .catch((err) => {
            console.log(err)
        })
    }

    // useEffect(() => {
    //     axios.get("http://127.0.0.1:8000/api/user")

    //     .then((res) => {
    //         console.log(res)
    //     })

    //     .catch((err) => {
    //         console.log(err)
    //         navigate('/login')
    //     });
    //   }, []);

    return (
        <div>Userview
            <button onClick={logout} type='button'>Déconnexion</button>
        </div>
    )
}

export default Userview