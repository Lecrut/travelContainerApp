import flask
from openai import OpenAI


app = flask.Flask("__name__")


@app.route("/get_attractions", methods=["POST"])
def get():
    client = OpenAI()
    # try:
    data = flask.request.get_json(force=True)
    city_name = data['place']
    prompt = f"Tourist attractions in {city_name}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a tourist guide."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message["content"]
        # return city_name
    # except:
    #     return "Error occurred", 400


if __name__ == "__main__":
    app.run(port=4001, host="0.0.0.0")