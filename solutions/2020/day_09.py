from AoC.utils import get_input

xmas = get_input(9, lambda i: int(i))

for x, number in enumerate(xmas[25:]):
    preamble = xmas[x:x+25]
    pair = False
    for y, nr in enumerate(preamble):
        for x, another in enumerate(preamble):
            if x == y:
                continue
            if nr + another == number:
                pair = True
    if not pair:
        print('Part 1:', number)
        break

def count(number, index=0):
    accumulated = []
    for i in xmas[index:]:
        if i != number:
            accumulated.append(i)
        if sum(accumulated) == number:
            return min(accumulated) + max(accumulated)
    return count(number, index+1)

print('Part 2:', count(number))