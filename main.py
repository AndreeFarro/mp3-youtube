import socketio
import os

from flask import Flask
from src.sockets.events import sio
from src.routes.api import routes as rest
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
app = Flask(__name__)

app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
app.register_blueprint(rest)

if __name__ == '__main__':
    app.run(host=os.getenv('HOST'),port=os.getenv('PORT'))