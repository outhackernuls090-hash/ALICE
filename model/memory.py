import json
from ..config import CONFIG


class MemoryStore:
    def __init__(self):
        self.file = CONFIG["memory_file"]
        try:
            with open(self.file, "r") as f:
                self.memory = json.load(f)
        except:
            self.memory = []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.memory, f, indent=2)

    def add(self, user, action, tokens):
        entry = {
            "user": user,
            "action": action,
            "tokens": tokens
        }
        self.memory.append(entry)
        self.memory = self.memory[-CONFIG["max_memory"]:]
        self.save()

    def recent(self, n=10):
        return self.memory[-n:]
