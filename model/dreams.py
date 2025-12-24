import random
from config import CONFIG
from .model import BottomUpModel


class DreamEngine:
    """
    ALICE dreams by rearranging and recombining memories.
    This strengthens the associative graph.
    """

    def __init__(self, model):
        self.model = model

    def dream(self):
        if not self.model.vocab:
            return

        for _ in range(CONFIG["dream_iterations"]):
            tok = random.choice(list(self.model.vocab))
            nxt = random.choice(list(self.model.vocab))
            self.model.concepts[tok][nxt] += 0.1
