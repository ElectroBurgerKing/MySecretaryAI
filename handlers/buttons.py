from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.menu import (
    main_menu,
    memory_menu,
    settings_menu
)

from handlers.state import set_pending

from handlers.actions.memory import (
    get_memory,
    clear_memory
)

from handlers.actions.profile import get_profile_text

from handlers.actions.settings import (
    get_user_settings,
    update_setting
)

from handlers.actions.secretary import (
    secretary_info,
    toggle_secretary,
    set_secretary_style,
    set_secretary_mode,
    get_secretary
)


def secretary_keyboard():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "🟢 Вкл / Выкл",
            callback_data="sec_toggle"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "⚡ Режим",
            callback_data="sec_mode"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "😊 Стиль",
            callback_data="sec_style"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🧠 Память",
            callback_data="sec_memory"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )
    )

    return keyboard


def update_secretary_message(bot, call):
    bot.edit_message_text(
        secretary_info(call.message.chat.id),
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=secretary_keyboard()
    )


def send_main_menu(bot, chat_id):
    bot.send_message(
        chat_id,
        "🤖 Главное меню:",
        reply_markup=main_menu()
    )


def register_buttons(bot: TeleBot):

    @bot.callback_query_handler(func=lambda call: True)
    def callbacks(call):

        chat_id = call.message.chat.id

        # =========================
        # ГЛАВНОЕ МЕНЮ
        # =========================

        if call.data == "chat":

            bot.send_message(
                chat_id,
                "💬 Напиши мне сообщение — я отвечу."
            )

        elif call.data == "memory":

            bot.send_message(
                chat_id,
                "🧠 Управление памятью:",
                reply_markup=memory_menu()
            )

        elif call.data == "profile":

            bot.send_message(
                chat_id,
                get_profile_text(chat_id)
            )

        elif call.data == "settings":

            bot.send_message(
                chat_id,
                "⚙️ Настройки:",
                reply_markup=settings_menu()
            )

        elif call.data == "secretary":

            bot.send_message(
                chat_id,
                secretary_info(chat_id),
                reply_markup=secretary_keyboard()
            )

        elif call.data == "status":

            settings = get_user_settings(chat_id)
            secretary = get_secretary(chat_id)

            model = settings.get("model")

            if not model:
                model = "по умолчанию"

            status_text = (
                "📊 Статус Элло\n\n"
                f"🤖 Секретарь: "
                f"{'🟢 включён' if secretary['enabled'] else '🔴 выключен'}\n"
                f"🧠 Память: "
                f"{'🟢 включена' if settings.get('memory', True) else '🔴 выключена'}\n"
                f"😊 Стиль: {settings.get('style', 'friendly')}\n"
                f"⚡ Модель: {model}"
            )

            bot.send_message(
                chat_id,
                status_text
            )

        elif call.data == "help":

            bot.send_message(
                chat_id,
                "❓ Помощь\n\n"
                "💬 Чат — обычное общение с Элло.\n"
                "🧠 Память — факты, которые Элло запоминает.\n"
                "👤 Профиль — информация о тебе.\n"
                "⚙️ Настройки — настройки Элло.\n"
                "🤖 AI-Секретарь — управление секретарём.\n"
                "📊 Статус — текущее состояние системы."
            )

        # =========================
        # ПАМЯТЬ
        # =========================

        elif call.data == "show_memory":

            bot.send_message(
                chat_id,
                get_memory(chat_id),
                reply_markup=memory_menu()
            )

        elif call.data == "add_memory":

            set_pending(
                chat_id,
                "add_memory"
            )

            bot.send_message(
                chat_id,
                "➕ Напиши факт в формате:\n\n"
                "name=Алексей\n\n"
                "Например:\n"
                "hobby=программирование"
            )

        elif call.data == "clear_memory":

            clear_memory(chat_id)

            bot.send_message(
                chat_id,
                "🗑 Память очищена.",
                reply_markup=memory_menu()
            )

        # =========================
        # НАСТРОЙКИ
        # =========================

        elif call.data == "settings_memory":

            settings = get_user_settings(chat_id)

            current = settings.get(
                "memory",
                True
            )

            update_setting(
                chat_id,
                "memory",
                not current
            )

            new_value = not current

            bot.send_message(
                chat_id,
                "🧠 Память: "
                + ("🟢 включена" if new_value else "🔴 выключена"),
                reply_markup=settings_menu()
            )

        elif call.data == "settings_style":

            settings = get_user_settings(chat_id)

            current = settings.get(
                "style",
                "friendly"
            )

            styles = [
                "friendly",
                "formal",
                "short"
            ]

            try:
                index = styles.index(current)
            except ValueError:
                index = 0

            new_style = styles[
                (index + 1) % len(styles)
            ]

            update_setting(
                chat_id,
                "style",
                new_style
            )

            names = {
                "friendly": "😊 Дружелюбный",
                "formal": "💼 Официальный",
                "short": "⚡ Короткий"
            }

            bot.send_message(
                chat_id,
                f"😊 Стиль изменён: {names[new_style]}",
                reply_markup=settings_menu()
            )

        elif call.data == "settings_model":

            settings = get_user_settings(chat_id)

            models = [
                "models/gemini-3.1-flash-lite",
                "models/gemini-flash-lite-latest",
                "models/gemini-3.5-flash-lite"
            ]

            current = settings.get("model")

            if current in models:
                index = models.index(current)
                new_model = models[
                    (index + 1) % len(models)
                ]
            else:
                new_model = models[0]

            update_setting(
                chat_id,
                "model",
                new_model
            )

            bot.send_message(
                chat_id,
                f"🤖 Модель изменена:\n\n{new_model}",
                reply_markup=settings_menu()
            )

        # =========================
        # СЕКРЕТАРЬ
        # =========================

        elif call.data == "sec_toggle":

            toggle_secretary(
                chat_id
            )

            update_secretary_message(
                bot,
                call
            )

        elif call.data == "sec_mode":

            current = get_secretary(
                chat_id
            )

            if current["mode"] == "auto":

                set_secretary_mode(
                    chat_id,
                    "analysis"
                )

            elif current["mode"] == "analysis":

                set_secretary_mode(
                    chat_id,
                    "draft"
                )

            else:

                set_secretary_mode(
                    chat_id,
                    "auto"
                )

            update_secretary_message(
                bot,
                call
            )

        elif call.data == "sec_style":

            current = get_secretary(
                chat_id
            )

            if current["style"] == "friendly":

                set_secretary_style(
                    chat_id,
                    "formal"
                )

            elif current["style"] == "formal":

                set_secretary_style(
                    chat_id,
                    "short"
                )

            else:

                set_secretary_style(
                    chat_id,
                    "friendly"
                )

            update_secretary_message(
                bot,
                call
            )

        elif call.data == "sec_memory":

            settings = get_secretary(
                chat_id
            )

            settings["memory"] = not settings["memory"]

            # Сохраняем изменение через secretary actions
            from handlers.actions.secretary import load_secretary, save_secretary

            data = load_secretary()
            data[str(chat_id)] = settings
            save_secretary(data)

            update_secretary_message(
                bot,
                call
            )

        # =========================
        # НАЗАД
        # =========================

        elif call.data == "back":

            bot.send_message(
                chat_id,
                "🤖 Главное меню:",
                reply_markup=main_menu()
            )

        # =========================
        # НЕИЗВЕСТНАЯ КНОПКА
        # =========================

        else:

            bot.send_message(
                chat_id,
                "⚠️ Эта кнопка пока не настроена."
            )

        # Telegram должен получить подтверждение
        # нажатия кнопки
        bot.answer_callback_query(
            call.id
        )