import socketio
import youtube_dl
import os
from datetime import datetime
from src.hooks.progress import progress
from src.http.response import response
import time



sio = socketio.Server(async_mode='threading',cors_allowed_origins="*")

@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')
    
@sio.event
def suma(sid):
    sio.emit("sends",{'a':"Hey soy el servidor"}, to=sid)


@sio.event
def down(sid,data):
    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)


    DIR_HASH = str(hash(datetime.now()))
    
    def hook(d): progress(d,sio,sid)

    ydl_opts = {
        'format': 'bestaudio/best/worst/worstaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        "noplaylist": True,
        'logger': MyLogger(),
        'progress_hooks': [hook],
        'outtmpl': './temp/'+DIR_HASH+'.%(ext)s'
    }
        
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as stream:
            stream.extract_info(data["url"], download=True)
    except:
        print("sd")
    else:      
        res = response("full download.", "http://127.0.0.1:5000/d/"+DIR_HASH+".mp3")       
        sio.emit("download", res , to=sid) 
        
        path = "./temp/"+DIR_HASH+".mp3"
        time.sleep(20)
        if os.path.exists(path):
            file = open(path,"r")
            if file.closed == False:
                file.close()
            os.remove(path)


@sio.event
def info(sid, data):
    ydl_opts = { 
                'format': 'bestaudio/best/worst/worstaudio',
                "noplaylist": True
                }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(data.get("url"), download=False)
    except youtube_dl.utils.DownloadError:
        sio.emit("data",{ "state" : False, 'music' : "not Found"}, to=sid)
    else:
        sio.emit("data",{ "state" : True , 'music' : info_dict }, to=sid)