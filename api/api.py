import flask
import openai
import os


app = flask.Flask("__name__")

key_api = os.environ["OPENAI_API_KEY"]

@app.route("/get_attractions", methods=["POST"])
def get():
    try:
        data = flask.request.get_json(force=True)
        city_name = data['place']
        question = f"Tourist attractions in {city_name}"

        client = openai.OpenAI(api_key=key_api)

        response = client.chat.completions.create(
        messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="gpt-3.5-turbo",
        )   

        return question + " " + response.choices[0].message.content, 200
    except:
        return "Error occurred", 400


if __name__ == "__main__":
    app.run(port=4001, host="0.0.0.0")