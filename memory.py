import json
import os

MEMORY_FILE = "users.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)


memory = load_memory()


def get_history(chat_id):
    chat_id = str(chat_id)

    if chat_id not in memory:
        memory[chat_id] = []

    return memory[chat_id]


def add_message(chat_id, role, content, max_history=20):
    chat_id = str(chat_id)

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
    memory[chat_id] = []
    save_memory(memory)
