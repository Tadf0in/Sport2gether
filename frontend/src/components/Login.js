import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import { client } from '../App'

function Login() {
    const navigate = useNavigate()
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [alert, setAlert] = useState('')

    const submitLogin = async (e) => {
        e.preventDefault()

        await client.post('/api/login', {
            username: email,
            password: password
        })
        .then((res) => {
            // navigate('/user')
            console.log(res)
        })
        .catch((err) => {
            console.log(err)
            setAlert("Adresse mail ou mot de passe incorrect")
        })
    }

    const alertDisplay = () => {
        if (alert !== '') {
            return <div className="alert alert-danger" role="alert">
                        {alert}
                    </div>
        }
    }

    useEffect(() => {
        setAlert('')
    }, [email, password])

    return (
        <div>
            {alertDisplay()}

            <form method='POST' onSubmit={submitLogin}>
            <div className="form-floating mb-3">
                <input type="email" placeholder='Email :' name='email' className="form-control" id="emailforminput"
                    value={email} onChange={e => setEmail(e.target.value)}
                />
                <label htmlFor="emailforminput">Email :</label>
            </div>
            <div className="form-floating mb-3">
                <input type="password" placeholder='Mot de passe :' name='password' className="form-control" id="passwordforminput"
                    value={password} onChange={e => setPassword(e.target.value)}

                />
                <label htmlFor="passwordforminput">Mot de passe :</label>
            </div>
            <button type="submit" className="btn btn-primary">Connexion</button>
            
            <br />
            <a href='/register'>Je n'ai pas de compte</a>
            </form>
        </div>
    )
}

export default Login