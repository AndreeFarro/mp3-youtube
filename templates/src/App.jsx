import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { socket } from './socket/config'
import './App.css'

import { Search } from './components/Search/Search'
import { Display } from './components/Display/Display'




function App() {


  socket.on('connect', () => {
    console.log('connected');
  });
  
  socket.on('disconnect', () => {
    console.log('disconnected');
  });


  return (
    <div className="App">
      <Search />
      <Display />
    </div>
  )
}

export default App
