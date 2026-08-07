import json
import os
from threading import Lock

# ВАЖНО: раньше этот файл назывался "users.json" — точно так же назывался
# файл в settings.py, и оба модуля независимо перезаписывали друг друга,
# гарантированно теряя данные (см. Ello 7.0 Technical Specification, F.1.1).
# Переносим историю диалогов в отдельный файл в data/, чтобы у каждого
# хранилища был свой файл.
MEMORY_FILE = "data/history.json"

_lock = Lock()


def _ensure_dir():
    directory = os.path.dirname(MEMORY_FILE)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_memory(memory):
    _ensure_dir()

    # Пишем во временный файл и атомарно переименовываем — это не решает
    # проблему гонок между несколькими процессами (нужен внешний lock/БД,
    # см. Phase 1 миграции), но защищает от битого файла при падении
    # процесса ровно в момент записи.
    tmp_path = MEMORY_FILE + ".tmp"

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)

    os.replace(tmp_path, MEMORY_FILE)


memory = load_memory()


def get_history(chat_id):
    chat_id = str(chat_id)

    with _lock:
        if chat_id not in memory:
            memory[chat_id] = []

        return list(memory[chat_id])


def add_message(chat_id, role, content, max_history=20):
    chat_id = str(chat_id)

    if content is None:
        return

    with _lock:
        if chat_id not in memory:
            memory[chat_id] = []

        memory[chat_id].append({
            "role": role,
            "content": content
        })

        memory[chat_id] = memory[chat_id][-max_history:]

        save_memory(memory)


def clear_history(chat_id):
    chat_id = str(chat_id)

    with _lock:
        memory[chat_id] = []
        save_memory(memory)
