import { useState } from 'react'
import './App.css'

import Cookies from 'js-cookie'
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Header from './components/Header'
import SignIn from './components/SignInForm';
import Home from './components/Home';
import Cart from './components/Cart';


function checkToken() {
  let token = Cookies.get('access_token')

  return token
}


function checkCart() {
    let cart = Cookies.get('cart')

    return cart
}


function App() {
  const [cart, setCart] = useState(checkCart())

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={ <Home /> }></Route>
          <Route path='/signin' element={ <SignIn /> }></Route>
          <Route path='/cart' element={ <Cart cart={ cart } /> }></Route>
        </Routes>
      </Router>
    </>
  )
}


export default App
