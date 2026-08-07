from profile import (
    get_all_facts,
    set_fact,
    clear_profile
)


def get_memory(chat_id):

    facts = get_all_facts(chat_id)

    if not facts:
        return "🧠 Память пустая."

    text = "🧠 Что я помню:\n\n"

    for key, value in facts.items():

        if isinstance(value, list):

            if value:
                text += (
                    f"• {key}: "
                    f"{', '.join(value)}\n"
                )

        else:

            text += (
                f"• {key}: {value}\n"
            )

    return text


def add_memory(chat_id, data):

    if "=" not in data:

        return (
            "❌ Неверный формат.\n\n"
            "Пример:\n"
            "name=Алексей"
        )

    key, value = data.split(
        "=",
        1
    )

    set_fact(
        chat_id,
        key.strip(),
        value.strip()
    )

    return "✅ Запомнил."


def clear_memory(chat_id):

    clear_profile(
        chat_id
    )

    return "🗑 Память очищена."