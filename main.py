import telebot

from telebot.types import ReplyKeyboardRemove

from config import BOT_TOKEN, BOT_NAME
from ai import ask_ai
from memory import clear_history
from utils import send_long_message

from handlers.menu import main_menu
from handlers.buttons import register_buttons
from handlers.state import pop_pending
from handlers.actions.memory import add_memory


# =========================
# Проверка конфигурации при старте
# =========================
# Раньше при отсутствующем BOT_TOKEN telebot.TeleBot(None) падал с
# малопонятной ошибкой библиотеки. Явная проверка сразу говорит,
# что именно не так.

if not BOT_TOKEN:
    raise RuntimeError(
        "Переменная окружения BOT_TOKEN не задана. "
        "Укажите токен Telegram-бота перед запуском."
    )


bot = telebot.TeleBot(BOT_TOKEN)


# =========================
# Подключаем кнопки
# =========================

register_buttons(bot)


# =========================
# START
# =========================

@bot.message_handler(commands=["start"])
def start(message):

    # Убираем старую нижнюю клавиатуру Telegram
    bot.send_message(
        message.chat.id,
        f"🤖 Запускаю {BOT_NAME}...",
        reply_markup=ReplyKeyboardRemove()
    )

    bot.send_message(
        message.chat.id,
        f"🤖 {BOT_NAME}\n\n"
        "👋 Привет!\n"
        "Я твой личный ИИ-секретарь.\n\n"
        "Выбери действие:",
        reply_markup=main_menu()
    )


# =========================
# Очистка истории
# =========================

@bot.message_handler(commands=["clear"])
def clear(message):

    clear_history(message.chat.id)

    bot.send_message(
        message.chat.id,
        "🧹 История очищена."
    )


# =========================
# Чат с ИИ (только текстовые сообщения)
# =========================
# Раньше catch-all хендлер не фильтровал content_types и получал
# message.text == None на фото/голосовых/файлах/стикерах, что тихо
# портило данные (в историю писался null). Теперь текстовые сообщения
# и остальные типы обрабатываются раздельно.

@bot.message_handler(content_types=["text"])
def chat(message):

    chat_id = message.chat.id

    # Если ждём ответ на конкретное действие (например "добавить факт
    # в память") — обрабатываем его здесь, а не отправляем в ИИ.
    pending_action = pop_pending(chat_id)

    if pending_action == "add_memory":
        result = add_memory(chat_id, message.text)
        bot.send_message(chat_id, result)
        return

    try:

        answer = ask_ai(chat_id, message.text)

        send_long_message(bot, chat_id, answer)

    except Exception as e:

        print(e)

        bot.send_message(
            chat_id,
            "⚠️ Ошибка при обращении к ИИ."
        )


# =========================
# Остальные типы сообщений — понятный ответ вместо тишины/падения
# =========================

@bot.message_handler(content_types=[
    "photo", "voice", "document", "sticker",
    "video", "audio", "video_note", "location", "contact"
])
def unsupported_content(message):

    bot.send_message(
        message.chat.id,
        "🙂 Пока я понимаю только текстовые сообщения.\n"
        "Голосовые сообщения и файлы появятся в одном из следующих обновлений."
    )


print(f"🚀 {BOT_NAME} started")


bot.infinity_polling()
