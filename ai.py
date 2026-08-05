from openai import OpenAI

from config import OPENAI_API_KEY, MODEL

from memory import add_message
from brain import build_prompt
from memory_ai import analyze_memory


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(chat_id, user_text):

    # Сначала пробуем сохранить важные факты
    try:
        analyze_memory(
            chat_id,
            user_text
        )
    except Exception:
        pass


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


    return (
        "Извини, я сейчас не смог нормально ответить. "
        "Попробуй ещё раз."
    )