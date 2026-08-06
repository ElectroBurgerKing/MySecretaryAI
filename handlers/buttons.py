from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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
            "🟢 Включить/Выключить",
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

    return keyboard



def register_buttons(bot: TeleBot):


    @bot.callback_query_handler(
        func=lambda call: True
    )
    def callbacks(call):

        chat_id = call.message.chat.id



        # Открытие секретаря

        if call.data == "secretary":

            bot.send_message(
                chat_id,
                secretary_info(chat_id),
                reply_markup=secretary_keyboard()
            )



        # Вкл / выкл

        elif call.data == "sec_toggle":

            status = toggle_secretary(chat_id)


            text = (
                "🤖 AI-Секретарь включён."
                if status
                else
                "🛑 AI-Секретарь выключен."
            )


            bot.send_message(
                chat_id,
                text
            )



        # Режим

        elif call.data == "sec_mode":

            current = get_secretary(chat_id)


            if current["mode"] == "auto":

                set_secretary_mode(
                    chat_id,
                    "analysis"
                )

                mode = "👀 Анализ"


            elif current["mode"] == "analysis":

                set_secretary_mode(
                    chat_id,
                    "draft"
                )

                mode = "📝 Черновики"


            else:

                set_secretary_mode(
                    chat_id,
                    "auto"
                )

                mode = "🤖 Автоответ"


            bot.send_message(
                chat_id,
                "⚡ Новый режим: " + mode
            )



        # Стиль

        elif call.data == "sec_style":

            current = get_secretary(chat_id)


            if current["style"] == "friendly":

                set_secretary_style(
                    chat_id,
                    "formal"
                )

                style = "💼 Официальный"


            elif current["style"] == "formal":

                set_secretary_style(
                    chat_id,
                    "short"
                )

                style = "⚡ Короткий"


            else:

                set_secretary_style(
                    chat_id,
                    "friendly"
                )

                style = "😊 Дружелюбный"


            bot.send_message(
                chat_id,
                "😊 Новый стиль: " + style
            )



        # Память

        elif call.data == "sec_memory":

            settings = get_secretary(chat_id)


            settings["memory"] = not settings["memory"]


            bot.send_message(
                chat_id,
                "🧠 Память секретаря: "
                + (
                    "🟢 включена"
                    if settings["memory"]
                    else
                    "🔴 выключена"
                )
            )



        bot.answer_callback_query(
            call.id
        )