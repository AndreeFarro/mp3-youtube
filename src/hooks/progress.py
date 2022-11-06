from src.helpers.format import clean_format_filename as clean
from src.http.response import response

STATUS_PROGRESS = 102

def progress(down_file ,sio, sid):
    if down_file.get('status') == 'finished':          
        open(down_file.get('filename'))      
        PATH_URL_FILE = "http://127.0.0.1:5000/d/" + clean(down_file.get('filename'))+".mp3"
        
    else:        
        res = response("downloading...", data_wait(down_file), STATUS_PROGRESS)
        print(down_file['_percent_str'])
        
        sio.emit("download.process", res , to=sid)
        
def data_wait(down):
    return {  
        "time"   : down.get("_eta_str"),
        "percent": down.get("_percent_str").strip(),
        "speed"  : down.get("_speed_str"),
        "bytes"  : down.get("_total_bytes_str")
    }