intents = [
    {"tag": "greet", "patterns": ["hello", "hi", "hey", "good morning"], "action": "greet"},
    {"tag": "protect", "patterns": ["danger", "attack", "enemy", "help"], "action": "protect"},
    {"tag": "analyze_user", "patterns": ["who are you", "what are you doing", "analyze me"], "action": "analyze_user"},
    {"tag": "ignore", "patterns": ["nothing", "leave me", "no action"], "action": "ignore"}
]

def get_action_from_input(user_input):
    user_input_lower = user_input.lower()
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in user_input_lower:
                return intent["action"]
    return "greet"
