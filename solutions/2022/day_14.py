from AoC.utils import solve
from collections import defaultdict

example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".splitlines()


def solution(puzzle_input: list[str], part_2: bool = False) -> int:
    matrix = defaultdict(dict)
    lowest_rock = None
    for path in puzzle_input:
        for i, (start_x, start_y) in enumerate(path[:-1]):
            end_x, end_y = path[i + 1]
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                    matrix[x][y] = True
                    if not lowest_rock or y > lowest_rock:
                        lowest_rock = y

    if part_2:
        lowest_rock += 2

    sand, current_y = 0, 0
    while current_y < lowest_rock and matrix.get(x):
        x = 500
        for y in range(0, lowest_rock + 1):
            if not part_2 or y + 1 != lowest_rock:
                if y + 1 < lowest_rock and not matrix[x].get(y + 1):
                    continue
                elif not matrix[x - 1].get(y + 1):
                    x -= 1
                    continue
                elif not matrix[x + 1].get(y + 1):
                    x += 1
                    continue

            if not matrix[x].get(y):
                sand += 1
                matrix[x][y] = True
                break
            elif not matrix[x - 1].get(y):
                sand += 1
                matrix[x - 1][y] = True
                break
            elif not matrix[x + 1].get(y):
                sand += 1
                matrix[x + 1][y] = True
                break
            current_y = y + 1
        if matrix[x].get(0):
            break

    return sand


solve(14, 1, solution, lambda x: [[int(n) for n in i.split(",")] for i in x.split(" -> ")], example, 24)
solve(14, 2, solution, lambda x: [[int(n) for n in i.split(",")] for i in x.split(" -> ")], example, 93, part_2=True)
