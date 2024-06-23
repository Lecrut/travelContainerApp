import datetime
import uuid

import flask
import flask_session
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = flask.Flask("__name__", template_folder="home/front/templates")

connection_uri = "http://connect:4002"
api_uri = "http://api:4001"

def get_mongo_client():
    uri = "mongodb://user:password@mongodb"
    mongo = MongoClient(uri, server_api=ServerApi("1"))    
    return mongo

def init_sessions(mongo):
    app.config["SESSION_TYPE"] = "mongodb"
    app.config["SESSION_MONGODB"] = mongo
    app.config["SESSION_MONGODB_DB"] = "travel"
    app.config["SESSION_MONGODB_COLLECT"] = "sessions"
    app.permament_session_lifetime = datetime.timedelta(hours=24)

    flask_session.Session(app)

def is_register():
    username = flask.request.form.get("username", "admin")
    password = flask.request.form.get("password", "password")

    response = requests.post(
        f"{connection_uri}/register",
        json={"username": username, "password": password},
    )

    if response.ok:
        return True
    return False

def is_signed():
    username = flask.request.form.get("username", "admin")
    password = flask.request.form.get("password", "password")

    response = requests.post(
        f"{connection_uri}/login",
        json={"username": username, "password": password},
    )

    if response.ok:
        return True
    return False

@app.route("/")
def index():
    if flask.session.get("is_logged_in", True):
        return flask.redirect("/form")
    
    return flask.render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST" and is_signed():
        flask.session["is_logged_in"] = True
        return flask.redirect("/")

    return flask.render_template("login.html")



@app.route("/register", methods=["POST", "GET"])
def register():
    if flask.request.method == "POST" and is_register():
        flask.session["is_logged_in"] = True
        return flask.redirect("/")

    return flask.render_template("register.html")


@app.route("/logout")
def logout():
    flask.session["is_logged_in"] = False
    return flask.redirect("/")

@app.route("/form")
def form():
    return flask.render_template("form.html")

@app.route("/get_attractions", methods=["POST"])
def get_attractions():
    city = flask.request.form.get("city", "")

    response = requests.post(
        f"{api_uri}/get_attractions",
        json={"place": city},
    )

    return flask.render_template("form.html", response = response.text)


if __name__ == "__main__":
    mongo = get_mongo_client()
    init_sessions(mongo)

    app.run(debug=True, port=4000, host="0.0.0.0")