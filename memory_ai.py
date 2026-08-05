from openai import OpenAI

from config import OPENAI_API_KEY, MODEL
from profile import set_fact


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def analyze_memory(chat_id, user_text):

    prompt = f"""
Проанализируй сообщение пользователя.

Твоя задача — найти важные факты, которые стоит запомнить навсегда.

Запоминай только:
- имя;
- возраст (если пользователь сам сказал);
- профессию;
- интересы;
- важные предпочтения.

Если есть факт для сохранения, верни строго в формате:

ключ=значение

Примеры:

name=Алексей
job=программист
hobby=игры

Если запоминать нечего — напиши:

none

Сообщение пользователя:

{user_text}
"""

    result = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = result.choices[0].message.content.strip()

    if answer.lower() == "none":
        return

    if "=" in answer:
        key, value = answer.split("=", 1)

        set_fact(
            chat_id,
            key.strip(),
            value.strip()
        )