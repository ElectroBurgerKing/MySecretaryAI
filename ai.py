import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    MODELS
)

from memory import add_message
from brain import build_prompt
from memory_ai import analyze_memory


genai.configure(
    api_key=GEMINI_API_KEY
)


def ask_ai(chat_id, user_text):


    # =========================
    # Анализ памяти
    # =========================

    try:

        analyze_memory(
            chat_id,
            user_text
        )

    except Exception as e:

        print(
            "Memory error:",
            e
        )


    # =========================
    # Создание контекста
    # =========================

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


    # =========================
    # Запуск моделей
    # =========================

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

            print(
                f"Модель {model_name} не сработала: {e}"
            )

            continue



    return (
        "⚠️ Сейчас не удалось подключиться к ИИ."
    )