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

        json.dump(
            profiles,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_profile(chat_id):

    chat_id = str(chat_id)

    if chat_id not in profiles:

        profiles[chat_id] = {
            "notes": [],
            "hobbies": []
        }

    return profiles[chat_id]


def set_fact(chat_id, key, value):

    profile = get_profile(chat_id)

    key = key.lower()

    if key == "note":

        if value not in profile["notes"]:
            profile["notes"].append(value)

    elif key == "hobby":

        if value not in profile["hobbies"]:
            profile["hobbies"].append(value)

    else:

        profile[key] = value

    save_profiles()


def get_fact(chat_id, key):

    profile = get_profile(chat_id)

    return profile.get(key)


def get_all_facts(chat_id):

    return get_profile(chat_id)