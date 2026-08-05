import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я Элло — твой ИИ-секретарь. Чем могу помочь?"
    )


@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        result = client.chat.completions.create(
            model="google/gemini-2.0-flash-exp:free",
            messages=[
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        )

        answer = result.choices[0].message.content
        bot.send_message(message.chat.id, answer)

    except Exception as e:
        bot.send_message(
            message.chat.id,
            "Ошибка ИИ: " + str(e)
        )


print("Ello is starting...")

bot.infinity_polling()
