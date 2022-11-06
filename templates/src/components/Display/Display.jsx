import React, { useEffect, useRef, useState } from 'react'
import { socket } from '../../socket/config';

export const Display = () => {

   const [music, setMusic] = useState({})
   useEffect(()=>{
      socket.on('data', (data) => {
         if(data.state){
            console.log(data)
            setMusic(data.music)
         }
      });

      return ()=>{
         socket.off('data')
      }
   })
   
   return (
      <div>
         <div className="information">
            <h2 className="channel">{music.channel}</h2>
            <h3 className="title">{music.title}</h3>
         </div>
         <div className="disk">
            <img src={music.thumbnail} alt="" width="100px"/>
         </div>
         <div className="player">

         {
            music?.url &&( 
               <audio controls name="media" src={music.url} type={"audio/mp4"} />
            )
         }
         

         </div>
      </div>
   )
}
