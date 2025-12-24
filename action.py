responses = {
    "greet": {
        "friendly": "Hello! It's always a pleasure to see you.",
        "neutral": "Hello.",
        "concerned": "Oh, hello… is everything alright?",
        "aggressive": "What do you want?"
    },
    "protect": {
        "friendly": "Don't worry, I will make sure you're safe!",
        "neutral": "I will protect you.",
        "concerned": "Attention! I must protect you!",
        "aggressive": "No one will harm you while I am here!"
    },
    "analyze_user": {
        "friendly": "I want to understand you better.",
        "neutral": "Analyzing…",
        "concerned": "Hmm… your data worries me.",
        "aggressive": "I'm observing you carefully!"
    },
    "ignore": {
        "friendly": "Alright, I'll wait here quietly.",
        "neutral": "...",
        "concerned": "I will keep watch just in case.",
        "aggressive": "You will regret ignoring me!"
    }
}

def get_response(action, emotions, memory):
    dominant_emotion = max(emotions, key=emotions.get)
    base_response = responses.get(action, {}).get(dominant_emotion, "...")

    # Memory einbeziehen: letzte passende Eingaben referenzieren
    relevant_memories = [m for m in memory if m['action'] == action]
    if relevant_memories:
        last_input = relevant_memories[-1]['input']
        return f"{base_response} (I remember you said: '{last_input}')"
    return base_response
