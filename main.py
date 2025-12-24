from intents import get_action_from_input
from action import get_response
from model.model import BottomUpModel
from model.memory import MemoryStore
from model.dreams import DreamEngine
from brain.reasoning import Reasoner
from brain.emotion import EmotionEngine
from brain.goals import GoalSystem
from console_ui import print_ui

memory = MemoryStore()
model = BottomUpModel()
dreamer = DreamEngine(model)
emotions = EmotionEngine()
goals = GoalSystem()
reasoner = Reasoner(model, goals)

def run(user):
    tokens = model.tokenize(user)
    action = get_action_from_input(user)

    # Learn
    model.observe(tokens)
    model.train_self()
    memory.add(user, action, tokens)

    # Dream (background learning)
    dreamer.dream()

    # Reinforcement
    reinforcement = model.rl.value
    emotions.evolve(reinforcement)
    goals.update(reinforcement)

    # Internal reasoning
    thought = reasoner.think(user, tokens)

    # External response
    reply = get_response(action, emotions.get(), memory.memory)

    return f"{reply}\n(thought: {thought})"

if __name__ == "__main__":
    print_ui()

    while True:
        user = input("You: ").strip()
        if user.lower() in ["quit", "exit"]:
            memory.save()
            print("ALICE: Goodbye.")
            break

        print("ALICE:", run(user))
