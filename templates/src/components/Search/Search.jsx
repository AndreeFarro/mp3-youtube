import React, { useRef } from 'react'
import { socket } from '../../socket/config';
import styles from './Search.module.css'
import { AiOutlineSearch } from "react-icons/ai";


export const Search = () => {
  AiOutlineSearch
  const link_music = useRef("");

  const get_data_Music = () =>{
    let url_music = link_music.current.value
    socket.emit("info",{ url:url_music })
  }

  return (
    <div className={styles.container}>
      <input className={styles.search} type="text" ref={link_music} placeholder="https://www.youtube.com/watch?v=DAIxrSvq6bo"/>
      <button className={styles.btn} onClick={get_data_Music}><AiOutlineSearch className={styles.icon_lens}/></button>
    </div>
  )
}
