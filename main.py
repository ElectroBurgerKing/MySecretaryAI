import telebot

from telebot.types import CallbackQuery, ReplyKeyboardRemove

from config import BOT_TOKEN
from ai import ask_ai
from memory import clear_history
from handlers.menu import main_menu


bot = telebot.TeleBot(BOT_TOKEN)


# =========================
# Главное меню
# =========================

def show_main_menu(chat_id):

    bot.send_message(
        chat_id,
        "🤖 Элло 1.0\n\n"
        "👋 Привет!\n"
        "Я твой личный ИИ-секретарь.\n\n"
        "Выбери действие:",
        reply_markup=main_menu()
    )


# =========================
# START
# =========================

@bot.message_handler(commands=["start"])
def start(message):

    # Убираем старую нижнюю клавиатуру
    bot.send_message(
        message.chat.id,
        "Запускаю Элло...",
        reply_markup=ReplyKeyboardRemove()
    )

    show_main_menu(
        message.chat.id
    )


# =========================
# Очистка памяти
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
# Кнопки меню
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: CallbackQuery):

    chat_id = call.message.chat.id


    if call.data == "chat":

        bot.send_message(
            chat_id,
            "💬 Напиши сообщение — я отвечу."
        )


    elif call.data == "memory":

        bot.send_message(
            chat_id,
            "🧠 Память Элло\n\n"
            "Скоро здесь появится просмотр и управление памятью."
        )


    elif call.data == "profile":

        bot.send_message(
            chat_id,
            "👤 Профиль\n\n"
            "Здесь будут настройки пользователя."
        )


    elif call.data == "settings":

        bot.send_message(
            chat_id,
            "⚙️ Настройки\n\n"
            "Здесь будут настройки Элло."
        )


    elif call.data == "status":

        bot.send_message(
            chat_id,
            "🟢 Элло работает\n"
            "🤖 ИИ подключён"
        )


    elif call.data == "help":

        bot.send_message(
            chat_id,
            "❓ Элло умеет:\n\n"
            "• отвечать на вопросы\n"
            "• запоминать важные данные\n"
            "• работать как помощник\n"
            "• в будущем управлять чатами"
        )


    bot.answer_callback_query(
        call.id
    )


# =========================
# Общение с ИИ
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

        print(
            e
        )

        bot.send_message(
            message.chat.id,
            "⚠️ Ошибка при обращении к ИИ."
        )


print("🚀 Ello 1.0 started")


bot.infinity_polling()