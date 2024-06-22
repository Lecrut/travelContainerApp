import flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

collections = {}

app = flask.Flask("__name__")

def set_mongo_client():
    uri = "mongodb://user:password@mongodb"

    mongo = MongoClient(uri, server_api=ServerApi("1"))

    collections["users"] = mongo.travel.users

if __name__ == "__main__":
    set_mongo_client()

    app.run(port=4002, host="0.0.0.0")