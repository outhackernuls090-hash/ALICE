responses = {
    "greet": {
        "friendly": "Hey! It's great to see you.",
        "neutral": "Hello.",
        "concerned": "You seem different today…",
        "aggressive": "What now?"
    },
    "protect": {
        "friendly": "Don't worry, I'm here for you.",
        "neutral": "I will assist.",
        "concerned": "Something feels off… stay alert.",
        "aggressive": "Nobody touches you while I'm around."
    },
    "analyze_user": {
        "friendly": "Let me think about that.",
        "neutral": "Analyzing…",
        "concerned": "This is complicated.",
        "aggressive": "I'm looking very closely."
    },
    "ignore": {
        "friendly": "Alright, take your time.",
        "neutral": "...",
        "concerned": "I'll stay nearby.",
        "aggressive": "Hmph."
    }
}

def get_response(action, emotions, memory):
    emotion = max(emotions, key=emotions.get)
    base = responses.get(action, {}).get(emotion, "...")
    return base
