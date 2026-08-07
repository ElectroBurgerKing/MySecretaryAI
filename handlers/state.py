_pending_actions = {}

def set_pending(chat_id, action):
    """Сохраняет ожидающее действие для пользователя."""
    _pending_actions[chat_id] = action

def get_pending(chat_id):
    """Возвращает ожидающее действие, не удаляя его."""
    return _pending_actions.get(chat_id)

def pop_pending(chat_id):
    """Возвращает ожидающее действие и сразу удаляет его."""
    return _pending_actions.pop(chat_id, None)

def clear_pending(chat_id):
    """Удаляет ожидающее действие пользователя."""
    _pending_actions.pop(chat_id, None)
