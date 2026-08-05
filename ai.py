from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    MODEL,
    SYSTEM_PROMPT,
    MAX_HISTORY
)

from memory import (
    get_history,
    add_message
)

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(chat_id, user_text):
    history = get_history(chat_id)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_text
    })

    result = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    answer = result.choices[0].message.content

    add_message(chat_id, "user", user_text, MAX_HISTORY)
    add_message(chat_id, "assistant", answer, MAX_HISTORY)

    return answer
