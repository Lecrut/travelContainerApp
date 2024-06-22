import flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

collections = {}

app = flask.Flask("__name__")

def set_mongo_client():
    uri = "mongodb://user:password@mongodb"

    mongo = MongoClient(uri, server_api=ServerApi("1"))

    collections["users"] = mongo.travel.users


def isUserExists(userName):
    query = {"username": userName}
    document = collections["users"].find_one(query)

    return document


@app.route("/register", methods=["POST"])
def register():
    try:
        data = flask.request.get_json(force=True)

        username = data["username"]
        password = data["password"]

    except:
        return "Error", 400

    user = isUserExists(username)

    if user:
        return "Error", 400

    collections["users"].insert_one( 
        {
            "username": username,
            "password": password,
        }
    )

    return "Ok", 200


if __name__ == "__main__":
    set_mongo_client()

    app.run(port=4002, host="0.0.0.0")