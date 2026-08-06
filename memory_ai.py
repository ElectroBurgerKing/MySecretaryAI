import re

from profile import set_fact


def analyze_memory(chat_id, user_text):

    text = user_text.strip()
    lower = text.lower()


    # =====================
    # Имя + дополнительная информация
    # =====================

    name_match = re.search(
        r"меня зовут\s+([а-яa-zё\-]+)",
        lower
    )


    if name_match:

        name = name_match.group(1)


        set_fact(
            chat_id,
            "name",
            name.title()
        )


        # Если дальше есть профессия

        job_match = re.search(
            r"(я\s+)?(работаю|программист|разработчик|инженер|дизайнер|учусь)\s*(.*)",
            lower
        )


        if job_match:

            job = job_match.group(0)

            job = (
                job
                .replace("я", "")
                .replace("работаю", "")
                .strip()
            )


            if job:

                set_fact(
                    chat_id,
                    "job",
                    job
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
    # Работа / профессия
    # =====================

    job_patterns = [
        r"я\s+программист",
        r"я\s+разработчик",
        r"я\s+инженер",
        r"я\s+работаю\s+(.+)"
    ]


    for pattern in job_patterns:

        match = re.search(
            pattern,
            lower
        )


        if match:

            job = match.group(0)


            set_fact(
                chat_id,
                "job",
                job
            )

            return



    # =====================
    # Интересы
    # =====================

    hobby_match = re.search(
        r"(люблю|нравится|увлекаюсь)\s+(.+)",
        lower
    )


    if hobby_match:

        hobby = hobby_match.group(2)


        # Разделяем через запятую и "и"

        hobbies = re.split(
            r",| и | & ",
            hobby
        )


        for item in hobbies:

            item = item.strip()


            if item:

                set_fact(
                    chat_id,
                    "hobby",
                    item
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