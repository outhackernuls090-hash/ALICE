# intents.py
import re

def detect_intent(user_input):
    text = user_input.lower()

    # Begrüßung
    if re.search(r"\b(hello|hi|hey)\b", text):
        return "greeting"

    # Frage nach Alice
    if re.search(r"\b(who are you|your name)\b", text):
        return "ask_name"

    # Frage nach User
    if re.search(r"\b(who am i|my name)\b", text):
        return "ask_user"

    # Stimmung / Gefühle
    if re.search(r"\b(happy|sad|angry|tired|good|bad)\b", text):
        return "ask_feeling"

    # Korrektur
    if re.search(r"\b(no|actually|i mean)\b", text):
        return "correction"

    # Sonstiges / Default
    return "default"
