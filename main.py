import telebot

from telebot.types import CallbackQuery

from config import BOT_TOKEN
from ai import ask_ai
from memory import clear_history
from handlers.menu import main_menu


bot = telebot.TeleBot(BOT_TOKEN)


# ---------- START ----------

@bot.message_handler(commands=["start"])
def start(message):

    bot.send_message(
        message.chat.id,
        "🤖 Элло 1.0\n\n"
        "👋 Привет!\n"
        "Я твой личный ИИ-секретарь.\n\n"
        "Выбери действие:",
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


# ---------- Обработка кнопок ----------

@bot.callback_query_handler(func=lambda call: True)
def buttons(call: CallbackQuery):

    chat_id = call.message.chat.id


    if call.data == "chat":

        bot.send_message(
            chat_id,
            "💬 Напиши сообщение, и я отвечу."
        )


    elif call.data == "memory":

        bot.send_message(
            chat_id,
            "🧠 Раздел памяти.\n"
            "Скоро здесь можно будет смотреть и изменять сохранённые данные."
        )


    elif call.data == "profile":

        bot.send_message(
            chat_id,
            "👤 Профиль пользователя.\n"
            "Настройка профиля будет добавлена."
        )


    elif call.data == "settings":

        bot.send_message(
            chat_id,
            "⚙️ Настройки Элло.\n"
            "Скоро здесь появятся переключатели."
        )


    elif call.data == "status":

        bot.send_message(
            chat_id,
            "🟢 Элло работает.\n"
            "🤖 Искусственный интеллект подключён."
        )


    elif call.data == "help":

        bot.send_message(
            chat_id,
            "❓ Возможности Элло:\n\n"
            "• ответы на вопросы\n"
            "• память пользователя\n"
            "• личный помощник\n"
            "• будущий режим секретаря"
        )


    bot.answer_callback_query(call.id)


# ---------- Чат с ИИ ----------

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
            "⚠️ Ошибка обработки запроса."
        )


print("🚀 Ello 1.0 started")


bot.infinity_polling()