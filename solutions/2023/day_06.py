from AoC.utils import solve
from math import prod

example = """Time:      7  15   30
Distance:  9  40  200""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    ways = []
    for time, distance in zip(*puzzle_input):
        race = []
        for t in range(time):
            if t * (time - t) > distance:
                race.append(t)
        ways.append(len(race))

    return prod(ways)


solve(6, 1, solution, lambda x: [int(i.strip()) for i in x.split(" ")[1:] if i], example, 288)
solve(6, 2, solution, lambda x: [int(i.replace(" ", "").strip()) for i in x.split(":")[1:]], example, 71503)
