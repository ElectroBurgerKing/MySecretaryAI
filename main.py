import telebot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

from config import BOT_TOKEN
from ai import ask_ai
from memory import clear_history

bot = telebot.TeleBot(BOT_TOKEN)


# ---------- Главное меню ----------

def main_menu():

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row(
        KeyboardButton("🤖 Чат"),
        KeyboardButton("🧠 Память")
    )

    keyboard.row(
        KeyboardButton("👤 Профиль"),
        KeyboardButton("⚙️ Настройки")
    )

    keyboard.row(
        KeyboardButton("📊 Статус"),
        KeyboardButton("❓ Помощь")
    )

    return keyboard


# ---------- Команда START ----------

@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        "👋 Привет!\n\n"
        "Я Элло — твой личный ИИ-секретарь.\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_menu()
    )


# ---------- Очистка памяти ----------

@bot.message_handler(commands=["clear"])
def clear(message):

    clear_history(message.chat.id)

    bot.send_message(
        message.chat.id,
        "🧹 История очищена."
    )


# ---------- Кнопки ----------

@bot.message_handler(func=lambda m: m.text == "🧠 Память")
def memory_menu(message):

    bot.send_message(
        message.chat.id,
        "🧠 Скоро здесь будет управление памятью."
    )


@bot.message_handler(func=lambda m: m.text == "👤 Профиль")
def profile_menu(message):

    bot.send_message(
        message.chat.id,
        "👤 Скоро здесь будет профиль пользователя."
    )


@bot.message_handler(func=lambda m: m.text == "⚙️ Настройки")
def settings_menu(message):

    bot.send_message(
        message.chat.id,
        "⚙️ Скоро здесь появятся настройки."
    )


@bot.message_handler(func=lambda m: m.text == "📊 Статус")
def status_menu(message):

    bot.send_message(
        message.chat.id,
        "🟢 Элло работает.\n"
        "Модель Gemini активна."
    )


@bot.message_handler(func=lambda m: m.text == "❓ Помощь")
def help_menu(message):

    bot.send_message(
        message.chat.id,
        "Я могу:\n\n"
        "• отвечать на вопросы\n"
        "• запоминать важные факты\n"
        "• быть личным помощником"
    )


# ---------- Обычный чат ----------

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
            "⚠️ Временно не удалось получить ответ."
        )


print("🚀 Ello 4.0 started")

bot.infinity_polling()