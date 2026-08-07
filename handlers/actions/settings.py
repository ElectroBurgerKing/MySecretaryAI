import json
import os

FILE = "data/settings.json"

def load_settings():
    if not os.path.exists(FILE):
        return {}

    try:
        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

def save_settings(data):
    os.makedirs(
        os.path.dirname(FILE),
        exist_ok=True
    )

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

    user_id = str(chat_id)

    if user_id not in data:
        data[user_id] = {
            "memory": True,
            "style": "friendly"
        }

    data[user_id][key] = value

    save_settings(data)

def get_preferred_model(chat_id):
    """
    Возвращает модель Gemini, выбранную пользователем.

    Если пользователь ещё не выбирал модель,
    возвращается None — тогда ai.py использует
    первую модель из config.MODELS.
    """

    settings = get_user_settings(chat_id)

    return settings.get("model")
