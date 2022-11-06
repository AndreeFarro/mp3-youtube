import React, { useEffect, useState } from 'react'

export const Audio = ({music}) => {
   return (
         <audio controls name="media">
            <source src={music.url} type={"audio/mp4"} />
         </audio>
   )

}
