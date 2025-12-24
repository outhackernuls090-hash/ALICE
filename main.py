from model import SAO_ALICE
import time

alice = SAO_ALICE()
print("ALICE Fully Emergent English-like SAO AI started!\n")

while True:
    response = alice.interact()
    print("ALICE thinks:", response)
