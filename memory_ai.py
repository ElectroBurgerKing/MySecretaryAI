import re

from profile import set_fact


def analyze_memory(chat_id, user_text):

    text = user_text.strip()
    lower = text.lower()


    # =====================
    # Имя
    # =====================

    name_patterns = [

        r"меня зовут\s+([а-яa-zё\-]+)",

        r"(?:привет|здравствуй|это)?\s*я\s+([а-яa-zё\-]+)",

    ]


    for pattern in name_patterns:

        name_match = re.search(
            pattern,
            lower
        )


        if name_match:

            name = name_match.group(1).strip()


            bad_words = [
                "программист",
                "разработчик",
                "работаю",
                "люблю",
                "занимаюсь",
                "хочу",
                "думаю"
            ]


            if name not in bad_words:

                set_fact(
                    chat_id,
                    "name",
                    name.title()
                )


            break



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



    # =====================
    # Профессия
    # =====================

    job_patterns = [

        r"я\s+программист",

        r"я\s+разработчик",

        r"я\s+инженер",

        r"я\s+работаю\s+(.+)"

    ]


    for pattern in job_patterns:

        job_match = re.search(
            pattern,
            lower
        )


        if job_match:

            job = job_match.group(0).strip()


            set_fact(
                chat_id,
                "job",
                job
            )


            break



    # =====================
    # Интересы
    # =====================

    hobby_match = re.search(
        r"(люблю|нравится|увлекаюсь)\s+(.+)",
        lower
    )


    if hobby_match:

        hobbies_text = hobby_match.group(2)


        hobbies = re.split(
            r",| и ",
            hobbies_text
        )


        for hobby in hobbies:

            hobby = hobby.strip()


            if hobby:

                set_fact(
                    chat_id,
                    "hobby",
                    hobby
                )



    # =====================
    # Предпочтения
    # =====================

    preference_match = re.search(
        r"предпочитаю\s+(.+)",
        lower
    )


    if preference_match:

        preference = preference_match.group(1).strip()


        set_fact(
            chat_id,
            "preference",
            preference
        )



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