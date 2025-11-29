# action.py
import torch
import torch.nn.functional as F

def act(output_vector: torch.Tensor):
    probs = F.softmax(output_vector, dim=-1)           # Wahrscheinlichkeiten
    indices = torch.multinomial(probs, num_samples=output_vector.shape[1])
    vec = indices.squeeze().tolist()
    # Nur lesbare ASCII-Zeichen
    text = "".join([chr(max(32, min(int(x), 126))) for x in vec])
    print("ALICE:", text)
