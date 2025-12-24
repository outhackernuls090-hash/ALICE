from ..model.world_model import WorldModel

class Reasoner:
    """
    ALICE's internal reasoning engine.
    Builds 'thoughts' using the world model and generative model.
    """

    def __init__(self, model, goals):
        self.model = model
        self.goals = goals

    def think(self, user_input, tokens):
        # Top active goal
        goal = self.goals.top_goal()

        # Predict next symbolic event
        pred = self.model.world.predict(tokens)

        # Generate associative sentence
        seed = tokens[0] if tokens else None
        gen = self.model.generate(seed=seed)

        thought = (
            f"Goal: {goal}. "
            f"Prediction: {pred}. "
            f"Associations: {gen}."
        )

        return thought
