import random

class EmotionEngine:
    def __init__(self):
        self.state = {
            "friendly": 0.5,
            "neutral": 0.5,
            "concerned": 0.2,
            "aggressive": 0.1
        }

    def evolve(self, reinforcement):
        for k in self.state:
            self.state[k] += (random.uniform(-0.05, 0.05) + reinforcement/10)
            self.state[k] = max(0.0, min(1.0, self.state[k]))

    def get(self):
        return self.state
