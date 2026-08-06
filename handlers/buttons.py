from telebot import TeleBot
from telebot.types import CallbackQuery

from handlers.menu import (
    main_menu,
    memory_menu,
    settings_menu,
    secretary_menu
)

from handlers.actions.memory import (
    get_memory,
    clear_memory
)

from handlers.actions.profile import (
    get_profile_text
)

from handlers.actions.secretary import (
    get_secretary_status,
    enable_secretary
)

from handlers.actions.settings import (
    get_user_settings,
    update_setting
)


def register_buttons(bot: TeleBot):


    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call: CallbackQuery):

        chat_id = call.message.chat.id


        # 💬 Чат

        if call.data == "chat":

            bot.send_message(
                chat_id,
                "💬 Чат активен.\n"
                "Напиши сообщение — Элло ответит."
            )


        # 🧠 Память

        elif call.data == "memory":

            bot.send_message(
                chat_id,
                "🧠 Память Элло",
                reply_markup=memory_menu()
            )


        elif call.data == "show_memory":

            bot.send_message(
                chat_id,
                get_memory(chat_id)
            )


        elif call.data == "clear_memory":

            bot.send_message(
                chat_id,
                clear_memory(chat_id)
            )


        elif call.data == "add_memory":

            bot.send_message(
                chat_id,
                "➕ Отправь факт так:\n\n"
                "name=Алексей\n"
                "hobby=игры"
            )


        # 👤 Профиль

        elif call.data == "profile":

            bot.send_message(
                chat_id,
                get_profile_text(chat_id)
            )


        # ⚙️ Настройки

        elif call.data == "settings":

            settings = get_user_settings(chat_id)

            bot.send_message(
                chat_id,
                "⚙️ Настройки:\n\n"
                f"🧠 Память: {settings.get('memory')}\n"
                f"😊 Стиль: {settings.get('style')}",
                reply_markup=settings_menu()
            )


        elif call.data == "settings_memory":

            update_setting(
                chat_id,
                "memory",
                True
            )

            bot.send_message(
                chat_id,
                "🧠 Память включена."
            )


        elif call.data == "settings_style":

            update_setting(
                chat_id,
                "style",
                "friendly"
            )

            bot.send_message(
                chat_id,
                "😊 Стиль: дружелюбный."
            )


        elif call.data == "settings_model":

            bot.send_message(
                chat_id,
                "🤖 Сейчас используется Gemini."
            )


        # 🤖 Секретарь

        elif call.data == "secretary":

            bot.send_message(
                chat_id,
                get_secretary_status(chat_id),
                reply_markup=secretary_menu()
            )


        elif call.data == "secretary_on":

            bot.send_message(
                chat_id,
                enable_secretary(chat_id)
            )


        elif call.data == "secretary_settings":

            bot.send_message(
                chat_id,
                "⚙️ Настройки секретаря скоро подключим."
            )


        # 📊 Статус

        elif call.data == "status":

            bot.send_message(
                chat_id,
                "🟢 Элло работает\n\n"
                "🤖 Gemini: OK\n"
                "🧠 Память: OK\n"
                "⚙️ Система: OK"
            )


        # ❓ Помощь

        elif call.data == "help":

            bot.send_message(
                chat_id,
                "❓ Элло умеет:\n\n"
                "💬 Общаться\n"
                "🧠 Запоминать\n"
                "👤 Хранить профиль\n"
                "🤖 Готовиться стать секретарём"
            )


        # Назад

        elif call.data == "back":

            bot.send_message(
                chat_id,
                "🤖 Главное меню",
                reply_markup=main_menu()
            )


        bot.answer_callback_query(
            call.id
        )