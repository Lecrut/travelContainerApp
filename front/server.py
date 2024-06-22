import datetime
import uuid

import flask
import flask_session
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = flask.Flask("__name__", template_folder="home/front/templates")

connection_uri = "http://connect:4002"

def get_mongo_client():
    uri = "mongodb://user:password@mongodb"
    mongo = MongoClient(uri, server_api=ServerApi("1"))    
    return mongo

def init_sessions(mongo):
    app.config["SESSION_TYPE"] = "mongodb"
    app.config["SESSION_MONGODB"] = mongo
    app.config["SESSION_MONGODB_DB"] = "travelsDB"
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
    return flask.render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST" and is_signed():
        return flask.redirect("/")

    return flask.render_template("login.html")



@app.route("/register", methods=["POST", "GET"])
def register():
    if flask.request.method == "POST" and is_register():
        return flask.redirect("/")

    return flask.render_template("register.html")



@app.route("/logout")
def logout():
    return flask.redirect("/")


if __name__ == "__main__":
    mongo = get_mongo_client()
    init_sessions(mongo)

    app.run(debug=True, port=4000, host="0.0.0.0")