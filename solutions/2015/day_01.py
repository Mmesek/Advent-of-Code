from AoC.utils import solve


example = """()())""".splitlines()


def solution(puzzle_input: list[str]) -> int:
    floor, basement = 0, 0
    for x, step in enumerate(puzzle_input[0], start=1):
        floor += 1 if step == "(" else -1
        if not basement and floor == -1:
            basement = x
    return floor, basement


solve(1, 1, solution, lambda x: x, example, (-1, 5))
