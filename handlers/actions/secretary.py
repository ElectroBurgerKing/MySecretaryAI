import json
import os


SECRETARY_FILE = "data/secretary.json"



def load_secretary():

    if not os.path.exists(SECRETARY_FILE):

        return {}


    try:

        with open(
            SECRETARY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        return {}



def save_secretary(data):

    with open(
        SECRETARY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_secretary(chat_id):

    data = load_secretary()

    user_id = str(chat_id)


    if user_id not in data:

        data[user_id] = {

            "enabled": False,

            "mode": "auto",

            "style": "friendly",

            "memory": True,

            "allowed_chats": [],

            "blocked_chats": []

        }

        save_secretary(data)


    return data[user_id]



def toggle_secretary(chat_id):

    data = load_secretary()

    settings = get_secretary(chat_id)


    settings["enabled"] = not settings["enabled"]


    data[str(chat_id)] = settings


    save_secretary(data)


    return settings["enabled"]



def set_secretary_style(chat_id, style):

    data = load_secretary()

    settings = get_secretary(chat_id)


    settings["style"] = style


    data[str(chat_id)] = settings


    save_secretary(data)



def set_secretary_mode(chat_id, mode):

    data = load_secretary()

    settings = get_secretary(chat_id)


    settings["mode"] = mode


    data[str(chat_id)] = settings


    save_secretary(data)



def secretary_info(chat_id):

    settings = get_secretary(chat_id)


    status = (
        "🟢 Включён"
        if settings["enabled"]
        else
        "🔴 Выключен"
    )


    styles = {

        "friendly": "😊 Дружелюбный",

        "formal": "💼 Официальный",

        "short": "⚡ Короткий"

    }


    modes = {

        "auto": "🤖 Автоответ",

        "draft": "📝 Черновики",

        "analysis": "👀 Анализ"

    }


    return (

        "🤖 AI-Секретарь\n\n"

        f"Статус: {status}\n"

        f"Режим: {modes.get(settings['mode'])}\n"

        f"Стиль: {styles.get(settings['style'])}\n"

        f"Память: {'🟢' if settings['memory'] else '🔴'}"

    )