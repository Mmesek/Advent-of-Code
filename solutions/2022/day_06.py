from AoC.utils import solve


example = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
""".splitlines()


def solution(puzzle_input: list[str], distinct: int = 4) -> int:
    for x, _ in enumerate(puzzle_input[0][distinct:], distinct):
        if len(set(puzzle_input[0][x - distinct : x])) == distinct:
            return x


solve(6, 1, solution, lambda x: x, example, 7)
solve(6, 2, solution, lambda x: x, example, 19, distinct=14)
