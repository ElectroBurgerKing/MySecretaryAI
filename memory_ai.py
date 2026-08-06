import re

from profile import set_fact


def analyze_memory(chat_id, user_text):

    text = user_text.strip()
    lower = text.lower()


    # =====================
    # Имя
    # =====================

    name_patterns = [
        r"меня зовут (.+)",
        r"моё имя (.+)",
        r"мое имя (.+)",
        r"я (.+),? меня зовут"
    ]


    for pattern in name_patterns:

        match = re.search(
            pattern,
            lower
        )

        if match:

            name = match.group(1).strip()

            if name:

                set_fact(
                    chat_id,
                    "name",
                    name.title()
                )

            return



    # =====================
    # Возраст
    # =====================

    age = re.search(
        r"мне\s+(\d{1,3})\s*(лет|года|год)",
        lower
    )


    if age:

        set_fact(
            chat_id,
            "age",
            age.group(1)
        )

        return



    # =====================
    # Работа
    # =====================

    job_patterns = [
        "я работаю",
        "моя работа",
        "я занимаюсь"
    ]


    for phrase in job_patterns:

        if phrase in lower:

            job = text.lower().split(
                phrase,
                1
            )[1].strip()


            if job:

                set_fact(
                    chat_id,
                    "job",
                    job
                )

            return



    # =====================
    # Интересы
    # =====================

    hobby_patterns = [
        "я люблю",
        "мне нравится",
        "увлекаюсь",
        "мой интерес"
    ]


    for phrase in hobby_patterns:

        if phrase in lower:

            hobby = text.split(
                phrase,
                1
            )[1].strip()


            if hobby:

                set_fact(
                    chat_id,
                    "hobby",
                    hobby
                )

            return



    # =====================
    # Я предпочитаю
    # =====================

    if "предпочитаю" in lower:

        value = text.split(
            "предпочитаю",
            1
        )[1].strip()


        if value:

            set_fact(
                chat_id,
                "preference",
                value
            )

        return



    # =====================
    # Запомни
    # =====================

    if lower.startswith("запомни"):

        note = text[7:].strip()


        if note:

            set_fact(
                chat_id,
                "note",
                note
            )

        return