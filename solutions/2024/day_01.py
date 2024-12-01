from AoC.utils import solve


example = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()


def split_input(puzzle_input: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    left, right = [], []
    for a, b in puzzle_input:
        left.append(a)
        right.append(b)
    return left, right


def solution(puzzle_input: list[tuple[int, int]]) -> int:
    left, right = split_input(puzzle_input)
    left.sort()
    right.sort()
    distance = 0
    for a, b in zip(left, right):
        distance += abs(b - a)

    return distance


def solution_2(puzzle_input: list[tuple[int, int]]) -> int:
    left, right = split_input(puzzle_input)
    similarity = 0
    for n in left:
        similarity += n * right.count(n)
    return similarity


solve(1, 1, solution, lambda x: [int(i) for i in x.split("   ")], example, 11)
solve(1, 2, solution_2, lambda x: [int(i) for i in x.split("   ")], example, 31)
