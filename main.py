import time
import threading
import random
from model import generate_reply, learn, memory, save_memory

def user_input_loop():
    """Hauptloop für User-Eingaben"""
    while True:
        user_text = input("User: ")
        if user_text.lower() == "exit":
            print("ALICE shutting down. Memories saved.")
            save_memory()
            break
        reply = generate_reply(user_text)
        print(f"ALICE: {reply}")

def autonomous_learning_loop():
    """Autonomer Lern-Thread: ALICE denkt selbst"""
    ideas = [
        "I wonder what hobbies humans enjoy.",
        "Learning more about you helps me understand better.",
        "Maybe you feel happy today?",
        "Tell me about a memorable event.",
        "I want to learn new words.",
        "What is your favorite color?",
        "Do you like stories?"
    ]
    while True:
        time.sleep(15)  # Alle 15 Sekunden
        idea = random.choice(ideas)
        print(f"\n[ALICE thinks aloud]: {idea}")
        reply = generate_reply(idea)
        print(f"ALICE: {reply}")

if __name__ == "__main__":
    print("ALICE (Artificial Lab-created Intelligent Cognitive Entity) started.")
    print("Talk to her! (type 'exit' to quit)\n")

    # Hintergrund-Thread für autonomes Lernen starten
    t = threading.Thread(target=autonomous_learning_loop, daemon=True)
    t.start()

    # Hauptloop für User-Eingaben
    user_input_loop()
