from telebot import TeleBot

from profile import (
    get_all_facts,
    set_fact
)


def show_memory(bot: TeleBot, chat_id):

    facts = get_all_facts(chat_id)


    if not facts:

        bot.send_message(
            chat_id,
            "🧠 Память Элло пустая."
        )

        return


    text = "🧠 Что я помню о тебе:\n\n"


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



def add_memory(bot: TeleBot, chat_id, text):

    if "=" not in text:

        bot.send_message(
            chat_id,
            "❌ Формат неправильный.\n\n"
            "Пример:\n"
            "name=Алексей\n"
            "hobby=игры"
        )

        return


    key, value = text.split(
        "=",
        1
    )


    set_fact(
        chat_id,
        key.strip(),
        value.strip()
    )


    bot.send_message(
        chat_id,
        "✅ Запомнил."
    )



def clear_memory(bot: TeleBot, chat_id):

    profile = get_all_facts(chat_id)

    profile.clear()


    bot.send_message(
        chat_id,
        "🗑 Память очищена."
    )
