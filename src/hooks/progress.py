from src.helpers.format import clean_format_filename as clean
from src.http.response import response
import time
import os


STATUS_PROGRESS = 102

def progress(down_file ,sio, sid):
    if down_file.get('status') != 'finished':          
        res = response("downloading...", data_wait(down_file))
        print(down_file['_percent_str'])
        
        sio.emit("download.process", res , to=sid)
        
def data_wait(down):
    return {  
        "time"   : down.get("_eta_str"),
        "percent": down.get("_percent_str").strip(),
        "speed"  : down.get("_speed_str"),
        "bytes"  : down.get("_total_bytes_str")
    }