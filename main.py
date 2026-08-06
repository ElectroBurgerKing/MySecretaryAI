import telebot

from telebot.types import ReplyKeyboardRemove

from config import BOT_TOKEN
from ai import ask_ai
from memory import clear_history

from handlers.menu import main_menu
from handlers.buttons import register_buttons


bot = telebot.TeleBot(BOT_TOKEN)


# =========================
# Подключаем кнопки
# =========================

register_buttons(bot)


# =========================
# START
# =========================

@bot.message_handler(commands=["start"])
def start(message):

    # Убираем старую нижнюю клавиатуру Telegram
    bot.send_message(
        message.chat.id,
        "🤖 Запускаю Элло...",
        reply_markup=ReplyKeyboardRemove()
    )


    bot.send_message(
        message.chat.id,
        "🤖 Элло 1.0\n\n"
        "👋 Привет!\n"
        "Я твой личный ИИ-секретарь.\n\n"
        "Выбери действие:",
        reply_markup=main_menu()
    )


# =========================
# Очистка истории
# =========================

@bot.message_handler(commands=["clear"])
def clear(message):

    clear_history(
        message.chat.id
    )

    bot.send_message(
        message.chat.id,
        "🧹 История очищена."
    )


# =========================
# Чат с ИИ
# =========================

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

        print(e)

        bot.send_message(
            message.chat.id,
            "⚠️ Ошибка при обращении к ИИ."
        )


print("🚀 Ello 1.0 started")


bot.infinity_polling()