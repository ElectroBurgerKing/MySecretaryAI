from openai import OpenAI

from config import OPENAI_API_KEY, MODEL

from memory import add_message
from brain import build_prompt


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(chat_id, user_text):

    messages = build_prompt(
        chat_id,
        user_text
    )

    for _ in range(2):

        result = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        answer = result.choices[0].message.content

        if answer:
            answer = answer.strip()

        # Защита от служебных сообщений
        if (
            answer
            and "User Safety:" not in answer
            and "Response Safety:" not in answer
            and len(answer) > 3
        ):
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


    fallback = (
        "Извини, я сейчас не смог нормально ответить. "
        "Попробуй ещё раз через несколько секунд."
    )

    return fallback
