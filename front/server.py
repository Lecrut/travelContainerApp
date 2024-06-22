import datetime
import uuid

import flask
import flask_session
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = flask.Flask("__name__", template_folder="home/front/templates")

collections = {}

def get_mongo_client():
    uri = "mongodb://user:password@mongodb"

    mongo = MongoClient(uri, server_api=ServerApi("1"))
    collections["users"] = mongo.travel.users
    
    return mongo

def init_sessions(mongo):
    app.config["SESSION_TYPE"] = "mongodb"
    app.config["SESSION_MONGODB"] = mongo
    app.config["SESSION_MONGODB_DB"] = "travelsDB"
    app.config["SESSION_MONGODB_COLLECT"] = "sessions"
    app.permament_session_lifetime = datetime.timedelta(hours=24)

    flask_session.Session(app)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return flask.render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    return flask.render_template("register.html")


@app.route("/logout")
def logout():
    return flask.redirect("/")


if __name__ == "__main__":
    mongo = get_mongo_client()
    init_sessions(mongo)

    app.run(debug=True, port=4000, host="0.0.0.0")