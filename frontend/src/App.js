// import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Routes, Route} from 'react-router-dom'
import Form from './components/questionnaire/Form';
import Login from './components/Login';
import Userview from './components/userview/Userview';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.withCredentials = true
const client = axios.create({
    baseURL: "http://127.0.0.1:8000",
    withCredentials: true
  })
export {client}

 
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/register' element={<Form />}/>
        <Route path='/login' element={<Login />}/>
        <Route path='/user' element={<Userview />}/>
      </Routes>
    </div>
  );
}

export default App;