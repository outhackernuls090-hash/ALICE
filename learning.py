# learning.py
import torch
import copy
from model import LocalTransformer
from sandbox import Sandbox

sandbox = Sandbox()

def evaluate(model, input_tensor, input_text):
    task = sandbox.get_task()
    output_tensor = model(input_tensor)
    output_text = "".join([chr(max(32, min(int(round(x)), 126))) for x in output_tensor.squeeze().tolist()])
    reward = sandbox.evaluate(task, output_text, input_text)
    return reward

def evolve(population, input_tensor, input_text, top_k=2, mutation_rate=0.05):
    scores = [evaluate(ind, input_tensor, input_text) for ind in population]
    top_individuals = [population[i] for i in sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]]

    new_population = []
    for parent in top_individuals:
        child = copy.deepcopy(parent)
        with torch.no_grad():
            for param in child.parameters():
                param.add_(torch.randn_like(param) * mutation_rate)
        new_population.append(child)
    return new_population
