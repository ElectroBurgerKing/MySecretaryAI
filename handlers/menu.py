from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    keyboard = InlineKeyboardMarkup()

    keyboard.row(
        InlineKeyboardButton(
            "🤖 Чат",
            callback_data="chat"
        ),
        InlineKeyboardButton(
            "🧠 Память",
            callback_data="memory"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            "👤 Профиль",
            callback_data="profile"
        ),
        InlineKeyboardButton(
            "⚙️ Настройки",
            callback_data="settings"
        )
    )

    keyboard.row(
        InlineKeyboardButton(
            "📊 Статус",
            callback_data="status"
        ),
        InlineKeyboardButton(
            "❓ Помощь",
            callback_data="help"
        )
    )

    return keyboard
