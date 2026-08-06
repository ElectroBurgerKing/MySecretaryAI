import json
import os


FILE = "data/settings.json"



def load_settings():

    if not os.path.exists(FILE):
        return {}

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_settings(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_user_settings(chat_id):

    data = load_settings()

    return data.get(
        str(chat_id),
        {
            "memory": True,
            "style": "friendly"
        }
    )



def update_setting(chat_id, key, value):

    data = load_settings()

    if str(chat_id) not in data:
        data[str(chat_id)] = {}

    data[str(chat_id)][key] = value

    save_settings(data)
