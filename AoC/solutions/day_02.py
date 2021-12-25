from collections import Counter
from AoC.utils import get_input

def answer(horizontal: int, depth: int):
    print("Horizontal:", horizontal)
    print("Depth:", depth)
    print("Result:", horizontal * depth)

directions = [(d, int(v)) for d, v in get_input(2, lambda x: x.split(" "))]

c = Counter({"aim": 0})
for direction, value in directions:
    c[direction] += value
    if direction == "forward":
        c["depth"] += value * abs(c["aim"])
    elif direction == "down":
        c["aim"] += value
    elif direction == "up":
        c["aim"] -= value

answer(c["forward"], abs(c["up"] - c["down"]))
answer(c["forward"], c["depth"])
