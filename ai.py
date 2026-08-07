import google.generativeai as genai

from config import (
    GEMINI_API_KEY,
    MODELS
)

from memory import add_message
from brain import build_prompt
from memory_ai import analyze_memory
from handlers.actions.settings import get_preferred_model


if not GEMINI_API_KEY:
    raise RuntimeError(
        "Переменная окружения GEMINI_API_KEY не задана. "
        "Укажите ключ Gemini API перед запуском."
    )


genai.configure(
    api_key=GEMINI_API_KEY
)


def _model_order(chat_id):
    """
    Пробуем сначала модель, которую пользователь выбрал в настройках
    (⚙️ Настройки → 🤖 Модель), затем остальные модели из config.MODELS
    как раньше — по порядку, без дублей.
    """
    preferred = get_preferred_model(chat_id)
    order = [preferred] + [m for m in MODELS if m != preferred]
    return order


def ask_ai(chat_id, user_text):

    if not user_text or not user_text.strip():
        return "🙂 Напишите, пожалуйста, сообщение текстом."

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

    for model_name in _model_order(chat_id):

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
