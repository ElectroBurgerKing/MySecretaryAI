import google.generativeai as genai

from config import GEMINI_API_KEY


genai.configure(
    api_key=GEMINI_API_KEY
)


def ask_ai(chat_id, user_text):

    models = genai.list_models()

    result = []

    for m in models:
        if "generateContent" in m.supported_generation_methods:
            result.append(m.name)

    return "\n".join(result)