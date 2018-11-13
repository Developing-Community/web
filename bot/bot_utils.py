import json

import requests

from web import settings


def bot_send_message(chat_ids, message, keyboard):
    data = json.dumps({
        'chat_ids': chat_ids,
        'message': message,
        'keyboard': keyboard
    })
    response = requests.post(url=settings.BOT_API_URL + '/send-message/',
                             json=data).json()
