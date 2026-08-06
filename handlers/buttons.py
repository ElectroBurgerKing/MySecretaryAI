from telebot import TeleBot
from telebot.types import CallbackQuery

from handlers.menu import (
    main_menu,
    memory_menu,
    settings_menu,
    secretary_menu
)


def register_buttons(bot: TeleBot):


    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: CallbackQuery):

        chat_id = call.message.chat.id


        if call.data == "chat":

            bot.send_message(
                chat_id,
                "💬 Режим чата включён.\n"
                "Напиши сообщение — я отвечу."
            )


        elif call.data == "memory":

            bot.send_message(
                chat_id,
                "🧠 Память Элло",
                reply_markup=memory_menu()
            )


        elif call.data == "profile":

            bot.send_message(
                chat_id,
                "👤 Профиль пользователя\n\n"
                "Здесь скоро появится информация о тебе."
            )


        elif call.data == "settings":

            bot.send_message(
                chat_id,
                "⚙️ Настройки Элло",
                reply_markup=settings_menu()
            )


        elif call.data == "secretary":

            bot.send_message(
                chat_id,
                "🤖 AI-Секретарь\n\n"
                "Статус: 🔴 Выключен",
                reply_markup=secretary_menu()
            )


        elif call.data == "status":

            bot.send_message(
                chat_id,
                "🟢 Элло работает\n"
                "🤖 Модель: Gemini\n"
                "🧠 Память: активна"
            )


        elif call.data == "help":

            bot.send_message(
                chat_id,
                "❓ Помощь Элло\n\n"
                "Я умею:\n"
                "• отвечать на вопросы\n"
                "• хранить память\n"
                "• работать как помощник\n"
                "• готовиться стать секретарём"
            )


        elif call.data == "back":

            bot.send_message(
                chat_id,
                "🤖 Главное меню",
                reply_markup=main_menu()
            )


        elif call.data == "show_memory":

            bot.send_message(
                chat_id,
                "🧠 Пока память пуста.\n"
                "Скоро подключим просмотр сохранённых данных."
            )


        elif call.data == "add_memory":

            bot.send_message(
                chat_id,
                "➕ Напиши факт, который нужно запомнить."
            )


        elif call.data == "clear_memory":

            bot.send_message(
                chat_id,
                "🗑 Очистка памяти будет подключена."
            )


        elif call.data.startswith("settings_"):

            bot.send_message(
                chat_id,
                "⚙️ Настройка выбрана.\n"
                "Функция будет подключена следующим этапом."
            )


        elif call.data.startswith("secretary_"):

            bot.send_message(
                chat_id,
                "🤖 Настройка секретаря выбрана.\n"
                "Скоро подключим реальные функции."
            )


        bot.answer_callback_query(call.id)