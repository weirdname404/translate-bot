#!/usr/bin/python3
import requests
import sys


# def detect_lang(text: str, hint: str) -> str:
#     data = {'key': api_key, 'text': text, 'hint': hint}
#     r = requests.post(API_URL + 'detect', params=data)
#     res_json = r.json()
#
#     return res_json['lang'] if res_json['code'] == 200 else ''

class TranslateApi:
    translate_api_url = "https://translate.yandex.net/api/v1.5/tr.json/"

    def __init__(self, translate_key):
        self.translate_key = translate_key

    def translate(self, text, lang):
        data = {"key": self.translate_key, "text": text, "lang": lang}
        res_json = self.post("translate", data)

        return res_json["text"] if res_json["code"] == 200 else res_json["message"]

    def get_langs(self):
        data = {"key": self.translate_key, "ui": "ru"}
        response = self.post("getLangs", data)

        return response["langs"]

    def post(self, method, data):
        r = requests.post(self.translate_api_url + method, params=data)
        return r.json()


class DictApi:
    dict_api_url = "https://dictionary.yandex.net/api/v1/dicservice.json/"

    def __init__(self, dict_key):
        self.dict_key = dict_key

    def lookup(self, text, lang):
        data = {"key": self.dict_key, "text": text, "lang": lang}
        r = requests.post(self.dict_api_url + "lookup", params=data)
        res_json = r.json()
        err_code = res_json.get("code", None)

        if err_code:
            return res_json["message"]

        return res_json


# def main():
#     default_lang = "ru"
#     dict_lang = "en-ru"
#     while True:
#         inp = input()
#         print(f"{translate(inp, default_lang)}\n\n")
#         print(f"{lookup(inp, dict_lang)}\n\n")
#
#
# if __name__ == "__main__":
#     main()
