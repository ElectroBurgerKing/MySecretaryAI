import re

from profile import set_fact


def analyze_memory(chat_id, user_text):

    text = user_text.strip()
    lower = text.lower()


    # Имя
    if "меня зовут" in lower:

        name = text.lower().split("меня зовут", 1)[1].strip()

        if name:
            set_fact(chat_id, "name", name.title())

        return


    # Возраст
    age = re.search(r"мне\s+(\d{1,3})\s*(лет|года|год)", lower)

    if age:

        set_fact(
            chat_id,
            "age",
            age.group(1)
        )

        return


    # Профессия
    if "я работаю" in lower:

        job = text.split("я работаю", 1)[1].strip()

        if job:
            set_fact(
                chat_id,
                "job",
                job
            )

        return


    # Интересы
    if "я люблю" in lower:

        hobby = text.split("я люблю", 1)[1].strip()

        if hobby:
            set_fact(
                chat_id,
                "hobby",
                hobby
            )

        return


    # Запомни ...
    if lower.startswith("запомни"):

        note = text[8:].strip()

        if note:
            set_fact(
                chat_id,
                "note",
                note
            )

        return