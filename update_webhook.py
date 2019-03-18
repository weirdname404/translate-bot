import requests
from pprint import pprint
from app import get_url, get_config


def main():
    config = get_config()
    url = f"{config['url']}/{config['bot_token']}"
    requests.post(get_url("setWebhook"), data={"url": url})
    r = requests.get(get_url("getWebhookInfo"))
    pprint(r.status_code)
    pprint(r.json())


if __name__ == "__main__":
    main()
