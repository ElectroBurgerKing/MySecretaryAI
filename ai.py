import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    MODEL
)

from memory import add_message
from brain import build_prompt


genai.configure(
    api_key=GEMINI_API_KEY
)


model = genai.GenerativeModel(
    MODEL
)


def ask_ai(chat_id, user_text):

    messages = build_prompt(
        chat_id,
        user_text
    )


    # Собираем историю в один текст для Gemini
    prompt = ""

    for message in messages:
        role = message["role"]
        content = message["content"]

        prompt += f"{role}: {content}\n"


    try:
        response = model.generate_content(
            prompt
        )

        answer = response.text.strip()


        if answer:

            add_message(
                chat_id,
                "user",
                user_text
            )

            add_message(
                chat_id,
                "assistant",
                answer
            )

            return answer


    except Exception as e:

        return (
            "Произошла ошибка при обращении к ИИ: "
            + str(e)
        )


    return "Я не смог получить ответ. Попробуй ещё раз."