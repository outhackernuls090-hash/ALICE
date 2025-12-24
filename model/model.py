import random
import numpy as np
from collections import defaultdict, deque
from config import CONFIG
from .clustering import ConceptClusterer
from .vector_memory import VectorMemory
from .world_model import WorldModel
from .reinforcement import ReinforcementLearner


class BottomUpModel:
    def __init__(self):
        self.vocab = set()
        self.memory_window = deque(maxlen=500)

        self.concepts = defaultdict(lambda: defaultdict(float))

        # Neural network
        size = 3000
        hidden = CONFIG["nn_hidden_size"]

        self.W1 = np.random.randn(size, hidden) * 0.01
        self.W2 = np.random.randn(hidden, size) * 0.01

        self.clusterer = ConceptClusterer()
        self.vector_mem = VectorMemory()
        self.world = WorldModel(self)
        self.rl = ReinforcementLearner()

    def tokenize(self, t):
        return [x for x in t.lower().split() if x]

    def observe(self, tokens):
        self.memory_window.append(tokens)
        self._learn_transitions(tokens)
        self.vocab.update(tokens)
        self.clusterer.update_clusters(self.vocab)
        self.rl.reward(+0.01)

    def _learn_transitions(self, tokens):
        for i in range(len(tokens)-1):
            a, b = tokens[i], tokens[i+1]
            self.concepts[a][b] += 1.0

    def train_self(self):
        if not self.memory_window:
            return

        tokens = random.choice(self.memory_window)
        for i in range(len(tokens)-1):
            x = hash(tokens[i]) % 3000
            y = hash(tokens[i+1]) % 3000

            h = np.tanh(self.W1[x])
            out = self.W2.T @ h
            probs = np.exp(out) / np.sum(np.exp(out))

            grad = probs
            grad[y] -= 1

            self.W2 -= 0.001 * np.outer(h, grad)
            self.W1[x] -= 0.001 * (1 - h*h) * (self.W2 @ grad)

    def _next(self, t):
        if t in self.concepts:
            return max(self.concepts[t], key=self.concepts[t].get)
        return random.choice(list(self.vocab))

    def generate(self, seed=None, n=10):
        if not self.vocab:
            return "..."

        if seed is None:
            seed = random.choice(list(self.vocab))

        out = [seed]
        cur = seed

        for _ in range(n):
            cur = self._next(cur)
            out.append(cur)

        out[0] = out[0].capitalize()
        return " ".join(out)
