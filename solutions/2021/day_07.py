from functools import cache
from AoC.utils import get_input

crabs = sorted(get_input(7, lambda x: [int(i) for i in x.split(",")])[0])


@cache
def consecutive_sums(n: int) -> int:
    return (n * (n + 1)) // 2


print(min([
    sum([abs(pos - crab) for crab in crabs])
    for pos in range(min(crabs), max(crabs)+1)
]))

print(min([
    sum([consecutive_sums(abs(pos - crab)) for crab in crabs])
    for pos in range(min(crabs), max(crabs)+1)
]))
