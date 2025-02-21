import random

QUICK_PICK_SIZE = 6
MAX_NUMBER = 45

def generate_quick_pick():
    return sorted(random.sample(range(1, MAX_NUMBER+1), QUICK_PICK_SIZE))

how_many = int(input("How many quick picks? "))
for _ in range(how_many):
    print(*generate_quick_pick())

