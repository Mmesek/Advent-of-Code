from AoC.utils import solve
from copy import copy

example = """125 17""".splitlines()


class X:
    value: int

    def __init__(self, value: int):
        self.value = value


def blink(stone: int, x: X, stones: list[int]):
    if stone == 0:
        stones[x.value] += 1
    elif not len(str(stone)) % 2:
        s = str(stone)
        stones[x.value] = int(s[: len(s) // 2])
        stones.insert(x.value + 1, int(s[len(s) // 2 :]))
        x.value += 1
    else:
        stones[x.value] *= 2024


def solution(puzzle_input: list[int], blinks: int = 25) -> int:
    stones = puzzle_input[0]
    for _ in range(blinks):
        _stones = copy(stones)
        x = X(0)
        for stone in stones:
            blink(stone, x, _stones)
            x.value += 1
        stones = _stones
    return len(stones)


solve(11, 1, solution, lambda x: [int(i) for i in x.split()], example, 55312)
solve(11, 2, solution, lambda x: [int(i) for i in x.split()], blinks=75)
