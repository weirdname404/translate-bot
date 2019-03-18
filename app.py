import sys
import requests
import json
from flask import Flask, request
from pprint import pprint
from ya_api import TranslateApi

app = Flask(__name__)


def get_config():
    try:
        with open("config.json") as f:
            config = json.loads(f.read())
    except FileNotFoundError as e:
        sys.exit(e)

    return config


config = get_config()
bot_token = config["bot_token"]


def get_url(method):
    return f"https://api.telegram.org/bot{bot_token}/{method}"


# DEFAULT TRANSLATION INTO RUSSIAN
def process_message(update):
    message = update["message"]
    response = {"chat_id": message["from"]["id"]}

    if "text" in message:
        user_text = message["text"]
        translated_text = translate_api.translate(user_text, "ru")
        response["text"] = translated_text

    else:
        response["text"] = "Sorry, but that kind of content is not supported."

    requests.post(get_url("sendMessage"), data=response)


def process_inline_query(update):
    inline_query = update["inline_query"]
    user_query = inline_query["query"]

    if user_query:
        presented_langs = ("ru", "en")
        results = []
        text = "Translated by Yandex.Translate"

        for i in range(len(presented_langs)):
            lang = presented_langs[i]
            translated_text = "".join(translate_api.translate(user_query, lang))
            result = {
                "type": "contact", "id": str(i),
                "first_name": lang, "phone_number": translated_text,
                "input_message_content": {"message_text": f"{user_query}\n\n{translated_text}"}
            }

            results.append(result)

        response = {"inline_query_id": inline_query["id"], "results": json.dumps(results)}
        r = requests.post(get_url("answerInlineQuery"), data=response)
        pprint(r.json())


@app.route(f"/{bot_token}", methods=["POST"])
def process_update():
    update = request.get_json()
    pprint(update)
    if "message" in update:
        process_message(update)
        return "OK", 200

    elif "inline_query" in update:
        process_inline_query(update)
        return "OK", 200

    else:
        return "Cannot process such JSON", 500


if __name__ == '__main__':
    translate_api = TranslateApi(config["ya_api_trnsl_key"])
    app.run(debug=True)
