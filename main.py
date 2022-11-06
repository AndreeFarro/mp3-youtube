import socketio

from flask import Flask
from src.sockets.events import sio
from src.routes.api import routes as rest

app = Flask(__name__)

app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
app.register_blueprint(rest)

if __name__ == '__main__':
    app.run(debug=True,port=5000)