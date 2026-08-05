import json
import os

PROFILE_FILE = "profile.json"


def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}

    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}


profiles = load_profiles()


def save_profiles():
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=4)


def get_profile(chat_id):
    chat_id = str(chat_id)

    if chat_id not in profiles:
        profiles[chat_id] = {}

    return profiles[chat_id]


def set_fact(chat_id, key, value):
    chat_id = str(chat_id)

    if chat_id not in profiles:
        profiles[chat_id] = {}

    profiles[chat_id][key] = value
    save_profiles()
