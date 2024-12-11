from AoC.utils import solve
from functools import cache

example = """125 17""".splitlines()


@cache
def blink(stone: int, x: int):
    if x == 0:
        return 1

    s = str(stone)
    l = len(s)
    if stone == 0:
        return blink(1, x - 1)
    elif not l % 2:
        return blink(int(s[: l // 2]), x - 1) + blink(int(s[l // 2 :]), x - 1)
    return blink(stone * 2024, x - 1)


def solution(puzzle_input: list[int], blinks: int = 25) -> int:
    stones = [blink(stone, x) for stone, x in zip(puzzle_input[0], [blinks] * blinks)]
    return sum(stones)


solve(11, 1, solution, lambda x: [int(i) for i in x.split()], example, 55312)
solve(11, 2, solution, lambda x: [int(i) for i in x.split()], blinks=75)
