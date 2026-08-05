from config import SYSTEM_PROMPT, MAX_HISTORY
from memory import get_history
from profile import get_profile


def build_prompt(chat_id, user_text):
    history = get_history(chat_id)
    profile = get_profile(chat_id)

    profile_text = "Информация о пользователе отсутствует."

    if profile:
        profile_text = "\n".join(
            [
                f"{key}: {value}"
                for key, value in profile.items()
            ]
        )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # Добавляем профиль пользователя
    messages.append(
        {
            "role": "system",
            "content": (
                "Вот что ты знаешь о пользователе:\n"
                + profile_text
            )
        }
    )

    # Добавляем историю
    messages.extend(history[-MAX_HISTORY:])

    # Добавляем новое сообщение
    messages.append(
        {
            "role": "user",
            "content": user_text
        }
    )

    return messages
