from profile import get_all_facts


def get_profile_text(chat_id):

    profile = get_all_facts(chat_id)

    if not profile:
        return "👤 Профиль пуст."

    text = "👤 Профиль:\n\n"

    for key, value in profile.items():

        text += f"• {key}: {value}\n"


    return text
