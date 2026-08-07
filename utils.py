TELEGRAM_MAX_MESSAGE_LENGTH = 4096


def send_long_message(bot, chat_id, text, **kwargs):
    """
    Раньше bot.send_message() с ответом ИИ длиннее 4096 символов падал с
    ApiTelegramException, который ловился общим except в main.py и
    показывал пользователю "Ошибка при обращении к ИИ" — хотя ИИ
    отработал нормально, проблема была только в отправке. Эта функция
    режет длинный текст на части по границе символов и отправляет
    несколькими сообщениями.
    """
    if not text:
        text = "…"

    for i in range(0, len(text), TELEGRAM_MAX_MESSAGE_LENGTH):
        chunk = text[i:i + TELEGRAM_MAX_MESSAGE_LENGTH]
        bot.send_message(chat_id, chunk, **kwargs)
