import telebot

from config import BOT_TOKEN
from ai import ask_ai
from memory import clear_history

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я Элло — твой личный ИИ-секретарь."
    )


@bot.message_handler(commands=["clear"])
def clear(message):
    clear_history(message.chat.id)

    bot.send_message(
        message.chat.id,
        "🧹 Память очищена."
    )


@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        answer = ask_ai(
            message.chat.id,
            message.text
        )

        bot.send_message(
            message.chat.id,
            answer
        )

    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"Ошибка ИИ:\n{e}"
        )


print("🚀 Ello 3.0 started")

bot.infinity_polling()
