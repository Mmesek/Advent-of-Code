from AoC.utils import solve


example = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()


def get_difference(history: list[int], result: callable) -> list[int]:
    differences = [history[x + 1] - a for x, a in enumerate(history[:-1])]

    if len(set(differences)) == 1:
        return result(history, differences[0])
    return result(history, get_difference(differences, result))


def solution(puzzle_input: list[tuple[int]]) -> int:
    return sum(get_difference(history, lambda history, diff: history[-1] + diff) for history in puzzle_input)


def solution_2(puzzle_input: list[tuple[int]]) -> int:
    return sum(get_difference(history, lambda history, diff: history[0] - diff) for history in puzzle_input)


solve(9, 1, solution, lambda x: tuple(int(i) for i in x.split(" ")), example, 114)
solve(9, 2, solution_2, lambda x: tuple(int(i) for i in x.split(" ")), example, 2)
