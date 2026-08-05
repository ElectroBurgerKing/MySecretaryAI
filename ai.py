import google.generativeai as genai

from config import GEMINI_API_KEY, MODEL
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

    prompt = ""

    for message in messages:
        prompt += (
            message["role"]
            + ": "
            + message["content"]
            + "\n"
        )

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
            "Ошибка ИИ: "
            + str(e)
        )


    return "Не получилось получить ответ."