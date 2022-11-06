import React, { useRef } from 'react'
import { socket } from '../../socket/config';
import styles from './Search.module.css'

export const Search = () => {

  const link_music = useRef("");

  const get_data_Music = () =>{
    let url_music = link_music.current.value
    socket.emit("info",{ url:url_music })
    //socket.emit("down",{ url:url_music })
  }

  return (
    <div className={styles.search}>
      <input type="text" ref={link_music} />
      <button onClick={get_data_Music}>Buscar</button>
    </div>
  )
}
