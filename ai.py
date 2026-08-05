import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    MODELS
)

from memory import add_message
from brain import build_prompt


genai.configure(
    api_key=GEMINI_API_KEY
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


    last_error = None


    # Пробуем модели по очереди
    for model_name in MODELS:

        try:

            model = genai.GenerativeModel(
                model_name
            )


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

            last_error = e

            print(
                f"Модель {model_name} не сработала: {e}"
            )


            continue


    return (
        "Извините, у меня временные сложности с подключением. "
        "Попробуйте немного позже."
    )