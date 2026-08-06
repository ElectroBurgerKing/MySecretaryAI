import json
import os


USERS_FILE = "users.json"


def load_users():

    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as f:

        try:
            return json.load(f)

        except:
            return {}


users = load_users()


def save_users():

    with open(USERS_FILE, "w", encoding="utf-8") as f:

        json.dump(
            users,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_settings(chat_id):

    chat_id = str(chat_id)

    if chat_id not in users:

        users[chat_id] = {
            "memory": True,
            "emoji": True,
            "short_answers": False,
            "secretary_mode": False
        }

        save_users()

    return users[chat_id]


def set_setting(chat_id, key, value):

    settings = get_settings(chat_id)

    settings[key] = value

    save_users()


def get_setting(chat_id, key):

    settings = get_settings(chat_id)

    return settings.get(key)