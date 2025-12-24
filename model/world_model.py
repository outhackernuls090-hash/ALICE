class WorldModel:
    def __init__(self, model):
        self.model = model

    def predict(self, tokens):
        if not tokens:
            return "Something vague may happen."

        last = tokens[-1]
        if last in self.model.concepts:
            nxt = max(self.model.concepts[last], key=self.model.concepts[last].get)
            return f"'{last}' may lead to '{nxt}'."
        return "Uncertain future."
