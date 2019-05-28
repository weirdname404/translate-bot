# translate-bot
Telegram bot that uses [Yandex.Translate API](https://tech.yandex.ru/translate/) for text translation.

For proper work with APIs the app uses special tokens which should be described in `config.json`.
You should create config and make following structure:
```
{
  "url": HTTPS URL for Telegram Webhook,
  "bot_token": Telegram bot token,
  "ya_api_trnsl_key": Yandex.Translate API token,
}
```

Work is still in progress...
