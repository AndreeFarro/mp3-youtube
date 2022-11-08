import React, { useEffect, useRef, useState } from 'react'
import { socket } from '../../socket/config';

import "./Overwrite.scss";
import styles from "./Display.module.css";
import {AiOutlineDownload} from "react-icons/ai";
import AudioPlayer from 'react-h5-audio-player';

export const Display = () => {
   const [dict_music, setMusic] = useState({})
   const [progress, setProgress] = useState({})

   useEffect(()=>{
      socket.on('data', (data) => {
         if(data.state){
            console.log(data)
            setMusic(data.music)
         }
      });
      
      socket.on('download.process', (data)=>{
         if(data.state){
            console.log(data)
            setProgress(data)
            document.getElementById("down").style.width = data.data.percent

         }
      })

      socket.on('download', (data)=>{
         window.open(data.data)
         socket.emit("delete",{data: data.data})
      })

      return ()=>{
         socket.off('data')
         socket.off('download.process')
         socket.off('download')
      }

   })

   const download_Music = () =>{
      socket.emit("down",{ url:dict_music.url })
   }



   return (
      <div className={styles.container}>
         {
         dict_music?.url &&( 
         <>
            <div className={styles.information}>
               <h2 className={styles.channel}>{dict_music.channel}</h2>
               <h3 className={styles.title}>{dict_music.title}</h3>
            </div>
            <div className={styles.record}>
               <div className={styles.disk}>
                  <img src={dict_music.thumbnail} alt="" width="100px"/>
               </div>            
            </div>
            <div className={styles.player}>
                  <AudioPlayer src={dict_music.url} />
            </div>
            <div className={styles.download}>
               <button className={styles.btn} onClick={download_Music}>
                  <div>Descargar</div>   
                  <AiOutlineDownload className={styles.ico_download}/>
               </button>

               {
                  progress?.data &&( 
                  <div className={styles.progress}>
                     <div className={styles.progress_bar} id="down">
                        <span className={styles.progress_bar_text}>{progress.data.percent}</span>
                     </div>
                  </div>      
                  )
               }


            </div>

         </>
         )
      }
      </div>
   )
}
