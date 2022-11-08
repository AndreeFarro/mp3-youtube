from flask import Response, jsonify

def response(message: str, data, state: bool = True):
    return {    
        "state": state,
        "message": message,
        "data": data
    }