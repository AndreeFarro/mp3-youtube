from flask import Response, jsonify

def response(message: str, data, status: int = 200):
    return {    
        "status": status,
        "message": message,
        "data": data
    }