from flask import Blueprint, render_template, send_from_directory
from os import getcwd

routes = Blueprint("routes",__name__)



@routes.route("/")
def home():
    return send_from_directory("./templates/dist/", path="index.html",as_attachment=False)


@routes.route("/assets/<path:name>")
def js(name):
    return send_from_directory("./templates/dist/assets/", path=name,as_attachment=False)


@routes.route("/d/<path:time>")
def download_mp3(time):
    PATH_DOWN = time + ".mp3"
    
    PATH_TEMP = getcwd() + "/temp/" 
    return send_from_directory(PATH_TEMP, path=time,as_attachment=True)