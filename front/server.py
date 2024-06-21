import datetime
import uuid

import flask
import flask_session
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = flask.Flask("__name__", template_folder="home/app/templates")
database_base_url = "http://127.0.0.1:27018"
# api_base_url = "http://gierka-api:4002"


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
    app.run(port=4000, host="0.0.0.0")