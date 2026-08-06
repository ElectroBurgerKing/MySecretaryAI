from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    keyboard = InlineKeyboardMarkup()


    keyboard.row(
        InlineKeyboardButton(
            "💬 Чат",
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
            "🤖 AI-Секретарь",
            callback_data="secretary"
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



# Меню памяти

def memory_menu():

    keyboard = InlineKeyboardMarkup()


    keyboard.row(
        InlineKeyboardButton(
            "📋 Показать память",
            callback_data="show_memory"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "➕ Добавить факт",
            callback_data="add_memory"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "🗑 Очистить память",
            callback_data="clear_memory"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )
    )


    return keyboard



# Меню настроек

def settings_menu():

    keyboard = InlineKeyboardMarkup()


    keyboard.row(
        InlineKeyboardButton(
            "🧠 Память",
            callback_data="settings_memory"
        ),
        InlineKeyboardButton(
            "😊 Стиль",
            callback_data="settings_style"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "🤖 Модель",
            callback_data="settings_model"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )
    )


    return keyboard



# Меню секретаря

def secretary_menu():

    keyboard = InlineKeyboardMarkup()


    keyboard.row(
        InlineKeyboardButton(
            "🟢 Включить",
            callback_data="secretary_on"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "⚙️ Настройки ответов",
            callback_data="secretary_settings"
        )
    )


    keyboard.row(
        InlineKeyboardButton(
            "⬅️ Назад",
            callback_data="back"
        )
    )


    return keyboard