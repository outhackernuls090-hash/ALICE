# learning.py
import random
from collections import defaultdict, deque
from datetime import datetime
from typing import Dict, List

class SelfLearningModule:
    def __init__(self):
        self.concepts = defaultdict(lambda: defaultdict(float))
        self.memory = deque(maxlen=2000)
        self.vocabulary = set()

        self.action_weights = {
            "explore": 1.0,
            "analyze": 1.0,
            "connect": 1.0,
            "speak": 1.0
        }

    # ---------------------
    # Input processing
    # ---------------------
    def tokenize(self, text: str) -> List[str]:
        return [t for t in text.lower().split() if t.isalpha() or t.isalnum()]

    def create_input(self, text: str):
        tokens = self.tokenize(text)
        return {
            "tokens": tokens,
            "entities": [],
            "timestamp": datetime.now()
        }

    # ---------------------
    # Update learning
    # ---------------------
    def update_memory(self, new_input: dict, goals: Dict[str, float]):
        tokens = new_input["tokens"]

        for i in range(len(tokens) - 1):
            a, b = tokens[i], tokens[i + 1]
            self.concepts[a][b] += 1.0
            self.vocabulary.add(a)
            self.vocabulary.add(b)

        self.memory.append(new_input)

        for goal in goals:
            if random.random() < goals[goal]:
                self.reinforce_tokens(tokens)

    def reinforce_tokens(self, tokens: List[str]):
        for i in range(len(tokens) - 1):
            a, b = tokens[i], tokens[i + 1]
            self.concepts[a][b] *= 1.1

    # ---------------------
    # Action decision
    # ---------------------
    def decide_action(self, goals: Dict[str, float]):
        total = sum(self.action_weights.values())
        probs = [self.action_weights[a] / total for a in self.action_weights]
        return random.choices(list(self.action_weights.keys()), weights=probs)[0]

    # ---------------------
    # Generate human language
    # ---------------------
    def generate_human_language(self, action: str):
        if not self.memory:
            return "..."

        mem = random.choice(list(self.memory))
        tokens = mem["tokens"]
        sentence = []

        for t in tokens:
            if self.concepts[t]:
                next_tok = max(self.concepts[t], key=lambda k: self.concepts[t][k])
                sentence.append(next_tok)
            else:
                sentence.append(t)

        if sentence:
            sentence[0] = sentence[0].capitalize()

        if action == "speak":
            sentence.append("!")
        elif action == "explore":
            sentence.append(".")
        elif action == "analyze":
            sentence.append("...")

        return " ".join(sentence)

    # ---------------------
    # Self-learning
    # ---------------------
    def self_learn(self, new_input: dict, action: str):
        tokens = new_input["tokens"]

        for i in range(len(tokens)-1):
            a, b = tokens[i], tokens[i+1]
            self.concepts[a][b] *= 1.05

        if action in self.action_weights:
            self.action_weights[action] *= 1.05

        total = sum(self.action_weights.values())
        for k in self.action_weights:
            self.action_weights[k] /= total
