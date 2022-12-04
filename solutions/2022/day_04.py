from AoC.utils import solve


example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()


def solution(puzzle_input: list[list[int]]) -> tuple[int, int]:
    contains = 0
    overlaps = 0

    for x, y in puzzle_input:
        x = range(x[0], x[1] + 1)
        y = range(y[0], y[1] + 1)
        if x.start in y and x.stop - 1 in y or y.start in x and y.stop - 1 in x:
            contains += 1
        if x.start < y.stop and y.start < x.stop:
            overlaps += 1

    return contains, overlaps


solve(4, 1, solution, lambda x: [[int(n) for n in i.split("-")] for i in x.split(",")], example, (2, 4))
solve(4, 2, solution, lambda x: [[int(n) for n in i.split("-")] for i in x.split(",")], example, (2, 4))
