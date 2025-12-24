import numpy as np
from ..config import CONFIG

class VectorMemory:
    def __init__(self):
        self.file = CONFIG["vector_file"]
        try:
            self.vectors = np.load(self.file)
        except:
            self.vectors = np.zeros((0, CONFIG["embedding_dim"]))

        self.index = []  # link to memory entries

    def embed(self, tokens):
        # Fake local embeddings (random but deterministic)
        seed = sum(hash(t) for t in tokens)
        rs = np.random.RandomState(seed)
        return rs.rand(CONFIG["embedding_dim"])

    def add(self, tokens, memory_id):
        vec = self.embed(tokens)
        self.vectors = np.vstack([self.vectors, vec])
        self.index.append(memory_id)
        np.save(self.file, self.vectors)

    def search(self, tokens, topk=5):
        if len(self.vectors) == 0:
        return []


        query = self.embed(tokens)

        sims = np.dot(self.vectors, query) / (
            np.linalg.norm(self.vectors, axis=1) * np.linalg.norm(query)
        )

        idx = np.argsort(-sims)[:topk]
        return [self.index[i] for i in idx]
