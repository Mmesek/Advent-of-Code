from functools import reduce
from AoC.utils import solve as solver


def crawl(x: int, y: int, rows: list[list[int]], previous_value: int, traversed: set = None) -> int:
    """Crawl basin from starting position x,y increasing size on until hitting 9"""
    basin = 0
    if rows[y][x] == 9:
        return basin

    if not traversed:
        traversed = set()
    elif (x, y) in traversed:
        return basin

    previous_value = rows[y][x]
    traversed.add((x, y))

    basin += 1
    if x:
        basin += crawl(x - 1, y, rows, previous_value, traversed)
    if len(rows[y]) - 1 > x:
        basin += crawl(x + 1, y, rows, previous_value, traversed)
    if y:
        basin += crawl(x, y - 1, rows, previous_value, traversed)
    if len(rows) - 1 > y:
        basin += crawl(x, y + 1, rows, previous_value, traversed)
    return basin


def solve(rows: list[int]) -> tuple[int, int]:
    """Iterates over rows and columns in iterable
    Counts Low Points and Crawls Basins"""
    lows = []
    sizes = []
    for y, row in enumerate(rows):
        for x, i in enumerate(row):
            if (
                (not x or row[x - 1] > i)
                and (not y or rows[y - 1][x] > i)
                and (not len(row) - 1 > x or row[x + 1] > i)
                and (not len(rows) - 1 > y or rows[y + 1][x] > i)
            ):
                lows.append(i)
                sizes.append(crawl(x, y, rows, None))
    largest = sorted(sizes)
    return sum(lows) + len(lows), reduce(lambda x, y: x * y, largest[-3:])

example = """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()
solver(9, 1, solve, lambda x: [int(i) for i in x], example, (15,1134))
