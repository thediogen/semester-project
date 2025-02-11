import { useState } from 'react'
import './App.css'

import Cookies from 'js-cookie'
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Header from './components/Header'
import SignIn from './components/SignInForm';
import Home from './components/Home';


function checkToken() {
  let token = Cookies.get('access_token')

  return token
}


function App() {
  const [token, setToken] = useState(checkToken())

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/signin' element={<SignIn />}></Route>
        </Routes>
      </Router>
    </>
  )
}


export default App
