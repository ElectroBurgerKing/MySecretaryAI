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


# ---------- Кнопки меню ----------

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: CallbackQuery):

    chat_id = call.message.chat.id


    if call.data == "chat":

        bot.send_message(
            chat_id,
            "💬 Напишите сообщение, и я отвечу."
        )


    elif call.data == "memory":

        bot.send_message(
            chat_id,
            "🧠 Управление памятью скоро будет добавлено."
        )


    elif call.data == "profile":

        bot.send_message(
            chat_id,
            "👤 Профиль пользователя скоро будет доступен."
        )


    elif call.data == "settings":

        bot.send_message(
            chat_id,
            "⚙️ Настройки Элло скоро будут доступны."
        )


    elif call.data == "status":

        bot.send_message(
            chat_id,
            "🟢 Элло работает.\n"
            "🤖 AI-модель активна."
        )


    elif call.data == "help":

        bot.send_message(
            chat_id,
            "❓ Я умею:\n\n"
            "• отвечать на вопросы\n"
            "• запоминать важные факты\n"
            "• работать как личный помощник"
        )


    bot.answer_callback_query(call.id)


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