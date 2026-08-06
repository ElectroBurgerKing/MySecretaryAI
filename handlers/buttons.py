from telebot import TeleBot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
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


    return keyboard



def update_secretary_message(bot, call):

    bot.edit_message_text(

        secretary_info(
            call.message.chat.id
        ),

        chat_id=call.message.chat.id,

        message_id=call.message.message_id,

        reply_markup=secretary_keyboard()

    )



def register_buttons(bot: TeleBot):


    @bot.callback_query_handler(
        func=lambda call: True
    )
    def callbacks(call):

        chat_id = call.message.chat.id



        # Открытие меню секретаря

        if call.data == "secretary":

            bot.send_message(

                chat_id,

                secretary_info(chat_id),

                reply_markup=secretary_keyboard()

            )



        # Включение / выключение

        elif call.data == "sec_toggle":

            toggle_secretary(
                chat_id
            )


            update_secretary_message(
                bot,
                call
            )



        # Смена режима

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



        # Смена стиля

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



        # Память

        elif call.data == "sec_memory":

            settings = get_secretary(
                chat_id
            )


            settings["memory"] = not settings["memory"]


            update_secretary_message(
                bot,
                call
            )



        bot.answer_callback_query(
            call.id
        )