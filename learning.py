import random
from collections import defaultdict, deque
from datetime import datetime

class SelfLearningModule:
    def __init__(self):
        self.concepts = defaultdict(lambda: defaultdict(float))
        self.memory = deque(maxlen=2000)
        self.vocabulary = set()
        self.action_weights = {"explore":1.0, "analyze":1.0, "connect":1.0, "speak":1.0}

    # -----------------------------
    # Generate synthetic internal ideas
    # -----------------------------
    def generate_synthetic_input(self):
        if not self.memory:
            tokens = [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(3,7))]
        else:
            tokens = random.choice(self.memory)["tokens"]
            tokens = [t if random.random()>0.2 else random.choice("abcdefghijklmnopqrstuvwxyz") for t in tokens]
        return {"tokens": tokens, "entities": [], "timestamp": datetime.now()}

    # -----------------------------
    # Update memory & concepts
    # -----------------------------
    def update_memory(self, new_input, goals):
        tokens = new_input["tokens"]
        for i in range(len(tokens)-1):
            self.concepts[tokens[i]][tokens[i+1]] += 1.0
            self.vocabulary.add(tokens[i])
            self.vocabulary.add(tokens[i+1])
        self.memory.append(new_input)

        # Goal reinforcement
        for goal in goals:
            if random.random() < goals[goal]:
                self.reinforce_tokens(tokens)

    def reinforce_tokens(self, tokens):
        for i in range(len(tokens)-1):
            self.concepts[tokens[i]][tokens[i+1]] *= 1.1

    # -----------------------------
    # Choose action based on goals + memory
    # -----------------------------
    def decide_action(self, goals):
        total = sum(self.action_weights.values())
        probs = [self.action_weights[a]/total for a in self.action_weights]
        return random.choices(list(self.action_weights.keys()), weights=probs, k=1)[0]

    # -----------------------------
    # Generate human-understandable language
    # -----------------------------
    def generate_human_language(self, action, memory, goals):
        if not memory:
            return "..."

        # Pick a related memory
        mem = random.choice(list(memory))
        tokens = mem["tokens"]
        sentence = []

        for t in tokens:
            if self.concepts[t]:
                next_tok = max(self.concepts[t], key=lambda k: self.concepts[t][k])
                sentence.append(next_tok)
            else:
                sentence.append(t)

        # Capitalize first word
        if sentence:
            sentence[0] = sentence[0].capitalize()

        # Append action-based phrase
        if action=="speak":
            sentence.append("!")
        elif action=="explore":
            sentence.append(".")
        elif action=="analyze":
            sentence.append("...")

        return " ".join(sentence)

    # -----------------------------
    # Self-learning (adjust associations)
    # -----------------------------
    def self_learn(self, new_input, action):
        tokens = new_input["tokens"]
        for i in range(len(tokens)-1):
            # reinforce successful transitions
            self.concepts[tokens[i]][tokens[i+1]] *= 1.05

        # Adjust action weights dynamically
        if action in self.action_weights:
            self.action_weights[action] *= 1.05
        total = sum(self.action_weights.values())
        for k in self.action_weights:
            self.action_weights[k] /= total
