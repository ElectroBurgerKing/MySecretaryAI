from telebot import TeleBot
from telebot.types import CallbackQuery

from handlers.menu import (
    main_menu,
    memory_menu,
    settings_menu,
    secretary_menu
)

from profile import (
    get_all_facts,
    set_fact
)


def register_buttons(bot: TeleBot):


    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: CallbackQuery):

        chat_id = call.message.chat.id


        # Главное меню

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
                "Здесь будет информация о тебе."
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
                "🤖 Модель подключена\n"
                "🧠 Память активна"
            )


        elif call.data == "help":

            bot.send_message(
                chat_id,
                "❓ Возможности Элло:\n\n"
                "• чат с ИИ\n"
                "• память пользователя\n"
                "• настройки\n"
                "• режим секретаря"
            )


        # Память

        elif call.data == "show_memory":

            facts = get_all_facts(chat_id)


            if not facts:

                text = (
                    "🧠 Память пустая."
                )

            else:

                text = "🧠 Что я знаю о тебе:\n\n"


                for key, value in facts.items():

                    if isinstance(value, list):

                        if value:

                            text += (
                                f"• {key}: "
                                + ", ".join(value)
                                + "\n"
                            )

                    else:

                        text += (
                            f"• {key}: {value}\n"
                        )


            bot.send_message(
                chat_id,
                text
            )


        elif call.data == "add_memory":

            bot.send_message(
                chat_id,
                "➕ Напиши факт для сохранения.\n\n"
                "Например:\n"
                "hobby=игры\n"
                "name=Алексей"
            )


        elif call.data == "clear_memory":

            profile = get_all_facts(chat_id)

            profile.clear()

            bot.send_message(
                chat_id,
                "🗑 Память очищена."
            )


        # Назад

        elif call.data == "back":

            bot.send_message(
                chat_id,
                "🤖 Главное меню",
                reply_markup=main_menu()
            )


        # Остальные настройки пока оставляем

        elif call.data.startswith("settings_"):

            bot.send_message(
                chat_id,
                "⚙️ Этот раздел скоро подключим."
            )


        elif call.data.startswith("secretary_"):

            bot.send_message(
                chat_id,
                "🤖 Этот раздел скоро подключим."
            )


        bot.answer_callback_query(
            call.id
        )