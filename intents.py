intents = [
    {"tag": "greet", "patterns": ["hello", "hi", "hey"], "action": "greet"},
    {"tag": "help", "patterns": ["help", "assist"], "action": "protect"},
    {"tag": "analyze", "patterns": ["why", "what", "how", "who"], "action": "analyze_user"},
    {"tag": "ignore", "patterns": ["nothing", "leave"], "action": "ignore"},
]

def get_action_from_input(user_input):
    text = user_input.lower()
    for intent in intents:
        for p in intent["patterns"]:
            if p in text:
                return intent["action"]
    return "greet"
