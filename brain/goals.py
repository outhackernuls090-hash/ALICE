class GoalSystem:
    def __init__(self):
        self.goals = {
            "understand_user": 0.7,
            "improve_model": 0.6,
            "stay_safe": 0.4,
            "explore_language": 0.9
        }

    def update(self, reinforcement):
        for g in self.goals:
            self.goals[g] += reinforcement * 0.01
            self.goals[g] = max(0.1, min(1.0, self.goals[g]))

    def top_goal(self):
        return max(self.goals, key=self.goals.get)
