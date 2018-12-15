import vk_api
import time
import random
import commands
import json
import requests
# import speech
import apiai

vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
vk._auth_token()

def update_base():
    conn = sqlite3.connect('USERS.sqlite')
    cursor = conn.cursor()

    cur = conn.cursor()
    cur.execute("SELECT * FROM Us")
    rows = cur.fetchall()

    return rows


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_button(label="Помощь", color="primary")],
        [get_button(label="Казино всё", color="negative")],
        [get_button(label="Баланс", color="primary"), get_button(label="Профиль", color="default")],
        [get_button(label="Работать", color="positive"), get_button(label="Бонус", color="positive")],
        [get_button(label="Есть", color="default")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

print(update_base())
