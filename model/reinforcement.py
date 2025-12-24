class ReinforcementLearner:
    def __init__(self):
        self.value = 0.0

    def reward(self, signal: float):
        self.value += signal
        self.value = max(min(self.value, 5.0), -5.0)

    def state(self):
        if self.value > 2:
            return "motivated"
        elif self.value < -2:
            return "frustrated"
        return "neutral"
