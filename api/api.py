import flask


app = flask.Flask("__name__")

if __name__ == "__main__":
    app.run(port=4001, host="0.0.0.0")