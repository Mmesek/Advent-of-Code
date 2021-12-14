from typing import Counter

from AoC.utils import get_input

text = get_input(14)
template = text[0]
rules = {}
for line in text[1:]:
    if line:
        rule, insert = [i.strip() for i in line.split("->")]
        rules[rule] = insert

def grow(template):
    new_template = ""
    for x, char in enumerate(template):
        if x+1 == len(template):
            break
        combination = char+template[x+1]
        insert = rules[combination]
        if combination in rules:
            new_template += char + insert
    return new_template + template[-1]

for i in range(10):
    template = grow(template)

c = Counter(template)
most = sorted(list(c.values()))[-1]
least = sorted(list(c.values()))[0]
print(most-least)
